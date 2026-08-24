/* Color collection filter + generated swatch palettes — used on colors.html
   and anywhere a #swatchGrid / .generated-swatch is present. */
function filterColors(cat, btn){
  document.querySelectorAll('.cf-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('#swatchGrid .swatch').forEach(s => {
    s.classList.toggle('hide', cat !== 'all' && s.dataset.cat !== cat);
  });
}

(function(){
  const namedPalettes = {
    quicksilver:['#1d2025','#f3f4f4','#8e949b','#3f444b'],
    stonehenge:['#2b2d2c','#d8d0c2','#8b8578','#f1eadb'],
    'feather gray':['#34383d','#d9dbd8','#929892','#f3f2ea'],
    houndstooth:['#17191d','#f0ede5','#777b80','#c8c2b8'],
    'rocky ridge':['#2f3332','#a59a83','#6f7169','#e1d3b5'],
    'trail mix':['#2d2119','#9c7348','#574535','#d9bd8a'],
    'cabin fever':['#3a3029','#d9c3a0','#80654c','#f3e2c4'],
    'sand dollar':['#ddd3bd','#f5eddd','#9e967f','#c8b999'],
    shoreline:['#263842','#d9d6cb','#81929a','#eef0e7'],
    'tidal wave':['#172f42','#5d8aa4','#d8e0dc','#26333a'],
    soapstone:['#1d2226','#889096','#d5d2c8','#4e575b'],
    blizzard:['#f4f4ef','#b8c0c5','#696f78','#ffffff'],
    opal:['#d7dad8','#aeb7b5','#f4f1e8','#687176'],
    'moon mist':['#c7c8c0','#e9e5d7','#8a8d86','#535a5c'],
    caraway:['#3b352c','#bca578','#786953','#ded0ad'],
    woven:['#4b4136','#c5aa7f','#8b7458','#e8d0a4'],
    niagara:['#93aeb7','#e8ede9','#5d7881','#c7d4d6'],
    'oyster bay':['#c6c3b6','#ece7dc','#8d8a7c','#5b5d57'],
    'dove gray':['#a9aaa5','#e1ded5','#747775','#c8c7c0'],
    'morning mist':['#d6d4ca','#f1eee5','#9fa4a0','#737b7a'],
    'slate gray':['#333941','#6c737a','#a7adb0','#171b20'],
    'smoke cement':['#595f62','#bec1bd','#858b8d','#e0ddd2'],
    espresso:['#2b1d16','#6e4b34','#a27a58','#1a110d'],
    andromeda:['#17181d','#5b5768','#d6d0c7','#8e8796'],
    yukon:['#4b3b29','#b79562','#e0c48d','#786044'],
    'white vein':['#f2f0e7','#bfc0b9','#696d6d','#ffffff'],
    granite:['#4d5052','#b8b8b2','#7b7e7f','#e4e0d6'],
    feldspar:['#d3c4aa','#876d51','#efe1c4','#5d5142'],
    neptunite:['#14171b','#2f3c44','#6b7580','#0b0d10'],
    fossil:['#8b7d68','#d5c5a4','#4e4539','#eee1c2'],
    'beach sand':['#d7c49d','#f0dfb5','#a58b60','#70593b'],
    landslide:['#3c3329','#8a6b4b','#c19b6d','#5b4a38'],
    castlerock:['#4d514e','#8b8e86','#c0b9aa','#252927'],
    'muir woods':['#283024','#68704d','#a2936d','#151a13'],
    charcoal:['#16191c','#4c5257','#858b8f','#08090b'],
    'midnight sky':['#0b1020','#26375d','#626d8a','#05070f'],
    clay:['#714737','#b47757','#d6a27d','#41261e'],
    basalt:['#17191b','#52585c','#9da1a0','#060708']
  };
  const fallback = {
    flake:['#25282d','#dad8d0','#868b91','#f6f1e6'],
    multispec:['#34383d','#c6c3b8','#7e8587','#ece6d9'],
    natural:['#8a704c','#d3bd8d','#5e513f','#f0d9aa'],
    metallic:['#4d545e','#c7ccd2','#828a95','#f4f6f8'],
    solid:['#30343a','#626872','#171a1f','#b7bcc2'],
    stain:['#3a2417','#7b4b2b','#a76a3a','#20130c']
  };

  function paletteFor(name, cat){
    const key = name.toLowerCase().replace(/(?:flake|floor|blend|swatch|stoneflecks|coating|marble)/g,'').trim();
    return namedPalettes[key] || fallback[cat] || fallback.multispec;
  }

  document.querySelectorAll('.generated-swatch').forEach(chip => {
    const card = chip.closest('.swatch');
    const name = card?.querySelector('.swatch-name')?.textContent || chip.dataset.swatch || '';
    const cat = card?.dataset.cat || 'multispec';
    paletteFor(name, cat).forEach((color, i) => chip.style.setProperty(`--c${i + 1}`, color));
  });
})();
