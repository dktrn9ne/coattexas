async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      return res.status(500).json({ error: 'OPENAI_API_KEY is not configured.' });
    }

    const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
    const { image, surface, finish, topcoat } = body || {};
    if (!image || !surface || !finish || !topcoat) {
      return res.status(400).json({ error: 'Missing image, surface, finish, or topcoat.' });
    }

    const match = String(image).match(/^data:(image\/(?:png|jpeg|jpg|webp));base64,(.+)$/);
    if (!match) {
      return res.status(400).json({ error: 'Image must be a PNG, JPEG, or WebP data URL.' });
    }

    const mimeType = match[1] === 'image/jpg' ? 'image/jpeg' : match[1];
    const imageBuffer = Buffer.from(match[2], 'base64');
    const prompt = [
      'Create a realistic finished-project preview for Precision Coatings of Texas.',
      `Use the uploaded photo as the source image and transform the requested ${surface} only.`,
      `Apply a professional ${finish} coating with a ${topcoat} topcoat.`,
      'Preserve the room, layout, perspective, lighting, walls, objects, and camera angle.',
      'Do not add labels, text, watermarks, fake UI, people, vehicles, or extra objects.',
      'The result should look like a believable after photo from a contractor portfolio.'
    ].join(' ');

    const form = new FormData();
    form.append('model', 'gpt-image-1');
    form.append('image', new Blob([imageBuffer], { type: mimeType }), `project.${mimeType.split('/')[1]}`);
    form.append('prompt', prompt);
    form.append('size', '1024x1024');

    const openaiRes = await fetch('https://api.openai.com/v1/images/edits', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`
      },
      body: form
    });

    const data = await openaiRes.json();
    if (!openaiRes.ok) {
      const message = data?.error?.message || 'OpenAI image generation failed.';
      return res.status(openaiRes.status).json({ error: message });
    }

    const result = data?.data?.[0];
    if (result?.b64_json) {
      return res.status(200).json({ image: `data:image/png;base64,${result.b64_json}` });
    }
    if (result?.url) {
      return res.status(200).json({ image: result.url });
    }

    return res.status(502).json({ error: 'OpenAI did not return an image.' });
  } catch (err) {
    return res.status(500).json({ error: err.message || 'Unexpected preview generation error.' });
  }
}

module.exports = handler;
module.exports.config = {
  api: {
    bodyParser: {
      sizeLimit: '12mb'
    }
  }
};
