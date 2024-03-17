function compileIcons() {
  const icons = document.querySelectorAll('symbol');
  const spriteSheet = document.createElement('svg');
  spriteSheet.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
  spriteSheet.setAttribute('style', 'display:none;');

  const defs = document.createElement('defs');
  spriteSheet.appendChild(defs);

  icons.forEach(icon => {
    const id = icon.getAttribute('id');
    const viewBox = icon.getAttribute('viewBox');
    const use = document.createElement('use');
    use.setAttribute('href', `#${id}`);
    use.setAttribute('xlink:href', `#${id}`);
    use.setAttribute('width', '24');
    use.setAttribute('height', '24');

    const symbol = document.createElement('symbol');
    symbol.setAttribute('id', id);
    symbol.setAttribute('viewBox', viewBox);
    symbol.appendChild(use);

    defs.appendChild(symbol);
  });

  document.body.appendChild(spriteSheet);
}
