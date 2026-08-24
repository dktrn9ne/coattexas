/* Before/After comparison slider — auto-inits any #baSlider on the page. */
(function(){
  const slider = document.getElementById('baSlider');
  if (!slider) return;
  const after   = document.getElementById('baAfter');
  const divider = document.getElementById('baDivider');
  const handle  = document.getElementById('baHandle');
  let pos = 50, dragging = false;

  function setPos(p){
    pos = Math.max(2, Math.min(98, p));
    after.style.clipPath = `inset(0 0 0 ${pos}%)`;
    divider.style.left = pos + '%';
    handle.style.left = pos + '%';
    slider.setAttribute('aria-valuenow', Math.round(pos));
  }
  function posFromEvent(e){
    const rect = slider.getBoundingClientRect();
    const x = (e.touches ? e.touches[0].clientX : e.clientX) - rect.left;
    return (x / rect.width) * 100;
  }
  slider.addEventListener('pointerdown', e => { dragging = true; slider.setPointerCapture(e.pointerId); setPos(posFromEvent(e)); });
  slider.addEventListener('pointermove', e => { if (dragging) setPos(posFromEvent(e)); });
  slider.addEventListener('pointerup',   () => dragging = false);
  slider.addEventListener('pointercancel',() => dragging = false);
  slider.addEventListener('keydown', e => {
    if (e.key === 'ArrowLeft')  { setPos(pos - 4); e.preventDefault(); }
    if (e.key === 'ArrowRight') { setPos(pos + 4); e.preventDefault(); }
  });
  setPos(50);
})();
