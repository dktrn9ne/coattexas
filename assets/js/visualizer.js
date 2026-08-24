/* AI project visualizer — calls /api/generate-preview.js (OpenAI images/edits). */
(function(){
  const canvas = document.getElementById('visualizerCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const upload = document.getElementById('visualizerUpload');
  const title = document.getElementById('visualizerUploadTitle');
  const status = document.getElementById('visualizerStatus');
  const empty = document.getElementById('visualizerEmpty');
  const finish = document.getElementById('visualizerFinish');
  const gloss = document.getElementById('visualizerGloss');
  const finishPreview = document.getElementById('visualizerFinishPreview');
  const generateBtn = document.getElementById('visualizerGenerate');
  const downloadBtn = document.getElementById('visualizerDownload');
  const surfaceButtons = document.querySelectorAll('#visualizerSurface .viz-choice');
  let projectImage = null;
  let projectDataUrl = '';
  let generatedDataUrl = '';
  let activeSurface = 'Garage Floor';

  const finishes = {
    quicksilver: { name:'Quicksilver Flake', colors:['#2d3035','#f2f3f4','#8e949d','#111317'] },
    stonehenge: { name:'Stonehenge Flake', colors:['#333431','#d5d0c3','#8f8a7c','#f6f0df'] },
    shoreline: { name:'Shoreline Flake', colors:['#4c5962','#e3ded1','#a8b4ba','#26333b'] },
    chrome: { name:'Chrome Silver Metallic', colors:['#59606a','#d9dde3','#8b929d','#f7f9fb'] },
    copper: { name:'Copper Canyon Metallic', colors:['#522812','#c87838','#7c421e','#f0a15a'] },
    slate: { name:'Slate Gray Solid', colors:['#30343a','#5f6670','#1e2228'] },
    pearl: { name:'Pearl White Solid', colors:['#e9e5dc','#f8f6ef','#cfc9bd'] },
    'texas-sand': { name:'Texas Sand Natural Accent', colors:['#d2bd90','#a98758','#f0ddb3','#7f643d'] },
    walnut: { name:'Walnut Stain', colors:['#3b2416','#6f4327','#9a6335','#24160d'] },
    cabinet: { name:'Cabinet Enamel White', colors:['#efece4','#ffffff','#d8d4c8','#bcb7a8'] },
    'cabinet-dark': { name:'Cabinet Espresso Enamel', colors:['#2b1d16','#4a3226','#6e4b34','#1a110d'] }
  };

  function setStatus(message, tag){
    status.innerHTML = `${message} <span>${tag || 'AI PREVIEW'}</span>`;
  }

  function selectedFinish(){
    return finishes[finish.value] || finishes.quicksilver;
  }

  function updatePreview(){
    const f = selectedFinish();
    finishPreview.style.background = `linear-gradient(135deg, ${f.colors.join(',')})`;
  }

  function drawCoverImage(img){
    const cw = canvas.width, ch = canvas.height;
    const scale = Math.max(cw / img.width, ch / img.height);
    const dw = img.width * scale;
    const dh = img.height * scale;
    ctx.clearRect(0, 0, cw, ch);
    ctx.fillStyle = '#0d0e11';
    ctx.fillRect(0, 0, cw, ch);
    ctx.drawImage(img, (cw - dw) / 2, (ch - dh) / 2, dw, dh);
  }

  function drawImageFromDataUrl(dataUrl, done){
    const img = new Image();
    img.onload = () => {
      drawCoverImage(img);
      empty.style.display = 'none';
      downloadBtn.disabled = false;
      if (done) done();
    };
    img.onerror = () => setStatus('The generated image could not be displayed.', 'TRY AGAIN');
    img.src = dataUrl;
  }

  function fileToOptimizedDataUrl(file){
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => {
        const img = new Image();
        img.onload = () => {
          const maxSide = 1200;
          const scale = Math.min(1, maxSide / Math.max(img.width, img.height));
          const work = document.createElement('canvas');
          work.width = Math.round(img.width * scale);
          work.height = Math.round(img.height * scale);
          const workCtx = work.getContext('2d');
          workCtx.drawImage(img, 0, 0, work.width, work.height);
          resolve(work.toDataURL('image/png'));
        };
        img.onerror = () => reject(new Error('This image could not be loaded in the browser.'));
        img.src = reader.result;
      };
      reader.onerror = () => reject(new Error('This image could not be read.'));
      reader.readAsDataURL(file);
    });
  }

  async function loadFile(file){
    if (!file) return;
    if (!file.type.startsWith('image/')) {
      setStatus('Please upload an image file.', 'TRY AGAIN');
      return;
    }

    try {
      title.textContent = file.name;
      setStatus('Loading photo...', 'WORKING');
      projectDataUrl = await fileToOptimizedDataUrl(file);
      projectImage = new Image();
      projectImage.onload = () => {
        drawCoverImage(projectImage);
        empty.style.display = 'none';
        generatedDataUrl = '';
        downloadBtn.disabled = true;
        setStatus('Photo loaded. Click Generate Preview to create a new AI image.', 'READY');
      };
      projectImage.onerror = () => setStatus('This image could not be displayed.', 'TRY AGAIN');
      projectImage.src = projectDataUrl;
    } catch (err) {
      setStatus(err.message || 'This image could not be loaded.', 'TRY AGAIN');
    }
  }

  async function generatePreview(){
    if (!projectDataUrl) {
      setStatus('Upload a project photo first, then generate the preview.', 'PHOTO NEEDED');
      return;
    }

    const f = selectedFinish();
    const payload = {
      image: projectDataUrl,
      surface: activeSurface,
      finish: f.name,
      topcoat: gloss.options[gloss.selectedIndex].text
    };

    generateBtn.disabled = true;
    downloadBtn.disabled = true;
    setStatus('Generating a new AI preview image...', 'WORKING');

    try {
      const res = await fetch('/api/generate-preview', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok || !data.image) {
        throw new Error(data.error || 'The AI preview route did not return an image.');
      }
      generatedDataUrl = data.image;
      drawImageFromDataUrl(generatedDataUrl, () => {
        setStatus('AI preview generated. Download it or try another finish.', 'DONE');
      });
    } catch (err) {
      if (projectImage) drawCoverImage(projectImage);
      downloadBtn.disabled = true;
      setStatus(`${err.message} Make sure the site is deployed on Vercel with OPENAI_API_KEY set.`, 'API NEEDED');
    } finally {
      generateBtn.disabled = false;
    }
  }

  upload.addEventListener('change', e => loadFile(e.target.files[0]));
  finish.addEventListener('change', updatePreview);
  gloss.addEventListener('change', updatePreview);
  surfaceButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      surfaceButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeSurface = btn.dataset.value;
    });
  });
  generateBtn.addEventListener('click', generatePreview);
  downloadBtn.addEventListener('click', () => {
    if (!generatedDataUrl) return;
    const a = document.createElement('a');
    a.href = generatedDataUrl;
    a.download = 'precision-coatings-ai-preview.png';
    a.click();
  });
  updatePreview();
})();
