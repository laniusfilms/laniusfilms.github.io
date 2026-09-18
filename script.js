const links=[...document.querySelectorAll('a[href^="#"]')];
links.forEach(link=>link.addEventListener('click',e=>{const id=link.getAttribute('href');if(id.length>1){e.preventDefault();document.querySelector(id)?.scrollIntoView({behavior:'smooth'});}}));
