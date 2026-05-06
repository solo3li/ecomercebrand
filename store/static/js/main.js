document.addEventListener('DOMContentLoaded', () => {
    // Splash Screen Logic
    const splash = document.getElementById("splashScreen");
    if (splash) {
        if (!sessionStorage.getItem('hasSeenSplash')) {
            splash.style.display = 'flex';
            document.body.style.overflow = 'hidden';
            
            setTimeout(() => {
                splash.classList.add('hidden');
                document.body.style.overflow = '';
                sessionStorage.setItem('hasSeenSplash', 'true');
                
                setTimeout(() => {
                    splash.style.display = 'none';
                }, 1000);
            }, 2000);
        }
    }

    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Fade-in animations on scroll
    const faders = document.querySelectorAll('.fade-in');
    
    const appearOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, appearOptions);

    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
});
