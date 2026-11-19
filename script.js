/* Load YouTube only after a visitor chooses to play a film. */
(() => {
  if (!window.HTMLDialogElement) return;
  const dialog = document.createElement('dialog');
  dialog.className = 'film-player';
  dialog.setAttribute('aria-labelledby', 'player-title');
  dialog.innerHTML = '<div class="player-heading"><h2 id="player-title"></h2><button type="button" class="player-close" aria-label="Close video">Close ×</button></div><div class="player-stage"></div><p class="player-description"></p><a class="player-fallback" target="_blank" rel="noopener noreferrer">Open on YouTube ↗</a>';
  document.body.append(dialog);
  const stage = dialog.querySelector('.player-stage');
  const close = dialog.querySelector('.player-close');
  let trigger;
  document.addEventListener('click', event => {
    const link = event.target.closest('a[data-video-id]');
    if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
    const id = link.dataset.videoId;
    if (!/^[\w-]{11}$/.test(id)) return;
    event.preventDefault();
    trigger = link;
    const card = link.closest('.film-card, .project, .reel-preview');
    const description = link.dataset.videoDescription || card?.querySelector('.film-description, .project-text>p')?.textContent || '';
    const title = link.dataset.videoTitle || 'Film';
    dialog.querySelector('#player-title').textContent = title;
    dialog.querySelector('.player-description').textContent = description;
    dialog.querySelector('.player-fallback').href = link.href;
    dialog.classList.toggle('portrait-player', !!card?.classList.contains('portrait'));
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0&playsinline=1`;
    iframe.title = title + ' — YouTube video player';
    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    iframe.allowFullscreen = true;
    iframe.referrerPolicy = 'strict-origin-when-cross-origin';
    stage.replaceChildren(iframe);
    document.body.classList.add('player-open');
    dialog.showModal();
    close.focus();
  });
  close.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => {
    stage.replaceChildren(); // Stop playback and release the player immediately.
    document.body.classList.remove('player-open');
    trigger?.focus({preventScroll:true});
  });
})();
