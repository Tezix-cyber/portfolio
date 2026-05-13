// ===== DARK MODE =====
const themeBtn = document.getElementById('theme-toggle');

if (themeBtn) {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
    const saved = localStorage.getItem('theme');

    const applyTheme = (mode) => {
        const dark = mode === 'dark';
        document.body.classList.toggle('dark', dark);
        themeBtn.textContent = dark ? '🌙' : '☀️';
        localStorage.setItem('theme', dark ? 'dark' : 'light');
    };

    applyTheme(saved || (prefersDark.matches ? 'dark' : 'light'));

    themeBtn.addEventListener('click', () => {
        applyTheme(document.body.classList.contains('dark') ? 'light' : 'dark');
    });

    prefersDark.addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) applyTheme(e.matches ? 'dark' : 'light');
    });
}

// ===== ACTIVE NAV =====
const page = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a, .footer-col ul a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === page || (page === '' && href === 'index.html')) {
        link.classList.add('active');
    }
});

// ===== BACK TO TOP =====
const backToTopBtn = document.getElementById('back-to-top');
if (backToTopBtn) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    });
    backToTopBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const scrollToTop = () => {
            const currentPosition = document.documentElement.scrollTop || document.body.scrollTop;
            if (currentPosition > 1) {
                window.requestAnimationFrame(scrollToTop);
                window.scrollTo(0, Math.floor(currentPosition - currentPosition / 8));
            } else {
                window.scrollTo(0, 0);
            }
        };
        scrollToTop();
    });
}

// ===== SCROLL PROGRESS BAR =====
const progressBar = document.createElement('div');
progressBar.id = 'scroll-progress';
document.body.prepend(progressBar);

window.addEventListener('scroll', () => {
    const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const progress = (scrollTop / scrollHeight) * 100;
    progressBar.style.width = progress + '%';
});

// ===== 3D TILT & GLOW EFFECT =====
const tiltElements = document.querySelectorAll('.sae-card, .section-card, .comp-card, .block, .card, .hero-card, .bio-card, .objectif-card, .intro-card');
tiltElements.forEach(el => {
    el.addEventListener('mousemove', (e) => {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        // Coordonnées pour l'effet Glow
        el.style.setProperty('--mouse-x', `${x}px`);
        el.style.setProperty('--mouse-y', `${y}px`);
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = ((y - centerY) / centerY) * -4;
        const rotateY = ((x - centerX) / centerX) * 4;
        
        el.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
        el.style.transition = 'transform 0.1s';
        el.style.zIndex = '10';
    });
    
    el.addEventListener('mouseleave', () => {
        el.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
        el.style.transition = 'transform 0.5s ease-out';
        el.style.zIndex = '1';
    });
});

// ===== COPY EMAIL =====
document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const email = link.getAttribute('href').replace('mailto:', '');
        navigator.clipboard.writeText(email).then(() => {
            const originalText = link.innerHTML;
            link.innerHTML = '✅ Copié !';
            link.style.color = 'var(--teal)';
            link.style.fontWeight = 'bold';
            setTimeout(() => {
                link.innerHTML = originalText;
                link.style.color = '';
                link.style.fontWeight = '';
            }, 2000);
        });
    });
});
