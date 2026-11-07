(() => {
  const header = document.querySelector('.site-header');
  const progress = document.querySelector('.reading-progress');
  const menuButtons = [...document.querySelectorAll('.menu-toggle, [data-mobile-menu-trigger]')];
  const mobileMenu = document.querySelector('#mobile-menu');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Initialize Lenis Smooth Scrolling (luxurious inertial scroll as seen on luccimedia.com)
  let lenis = null;
  if (!reducedMotion && typeof window.Lenis !== 'undefined') {
    try {
      lenis = new window.Lenis({
        duration: 1.25,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        orientation: 'vertical',
        gestureOrientation: 'vertical',
        smoothWheel: true,
        wheelMultiplier: 1.0,
        touchMultiplier: 1.4,
      });

      function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
      }
      requestAnimationFrame(raf);
    } catch (err) {
      console.warn('Lenis init:', err);
    }
  }

  const setMenu = (open) => {
    if (!menuButtons.length || !mobileMenu) return;
    menuButtons.forEach((button) => {
      button.setAttribute('aria-expanded', String(open));
      button.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      if (button.hasAttribute('data-mobile-menu-trigger')) button.textContent = open ? 'Close' : 'Menu';
    });
    mobileMenu.hidden = !open;
    document.body.classList.toggle('menu-open', open);
  };

  menuButtons.forEach((button) => button.addEventListener('click', () => {
    setMenu(button.getAttribute('aria-expanded') !== 'true');
  }));
  mobileMenu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') setMenu(false);
  });
  window.addEventListener('resize', () => {
    if (window.innerWidth > 760) setMenu(false);
  });

  const revealItems = document.querySelectorAll('[data-reveal], .scroll-reveal, .reveal-stagger');
  if ('IntersectionObserver' in window && !reducedMotion) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    revealItems.forEach((item) => revealObserver.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }

  // --- HERO TYPEWRITER ANIMATION (The Social Agency inspired word-by-word typewriter) ---
  const typewriterRoot = document.querySelector('#hero-typewriter');
  if (typewriterRoot) {
    const textTarget = typewriterRoot.querySelector('#typewriter-text') || typewriterRoot;
    const phrases = [
      'A CREATIVE AND SOCIAL AGENCY FOR BEAUTY, WELLNESS AND LIFESTYLE BRANDS THAT REFUSE TO LOOK LIKE EVERYONE ELSE.',
      'STRATEGY, CREATIVE DIRECTION AND PRODUCTION UNDER ONE ROOF.',
      'BUILT FOR BRANDS READY TO BE THE NAME PEOPLE BRING UP FIRST.',
      'CREATIVE DIRECTION WITH A BUSINESS PLAN BEHIND IT.',
      'DON\'T FOLLOW INDUSTRY STANDARDS. WORK WITH THE TEAM CREATING THEM.',
      'PLANNED. PRODUCED. DIRECTED.'
    ];

    if (reducedMotion) {
      textTarget.textContent = phrases[0];
    } else {
      let phraseIdx = 0;
      let charIdx = 0;
      let isDeleting = false;
      const typeSpeed = 70;
      const deleteSpeed = 25;
      const holdTime = 1600;
      const pauseBeforeNext = 300;

      const typeLoop = () => {
        const current = phrases[phraseIdx];
        if (!isDeleting) {
          textTarget.textContent = current.substring(0, charIdx + 1);
          charIdx++;
          if (charIdx === current.length) {
            isDeleting = true;
            window.setTimeout(typeLoop, holdTime);
            return;
          }
          window.setTimeout(typeLoop, typeSpeed);
        } else {
          textTarget.textContent = current.substring(0, charIdx - 1);
          charIdx--;
          if (charIdx === 0) {
            isDeleting = false;
            phraseIdx = (phraseIdx + 1) % phrases.length;
            window.setTimeout(typeLoop, pauseBeforeNext);
            return;
          }
          window.setTimeout(typeLoop, deleteSpeed);
        }
      };

      window.setTimeout(typeLoop, 400);
    }
  }

  const heroVisual = document.querySelector('.hero-visual');
  const heroMain = document.querySelector('[data-hero-image="main"]');
  const heroTop = document.querySelector('[data-hero-image="top"]');
  const heroDetail = document.querySelector('[data-hero-image="detail"]');
  const heroCaption = document.querySelector('[data-hero-caption]');
  const heroStatus = document.querySelector('#hero-slide-status');
  const heroIndex = document.querySelector('.visual-index');
  const slideButtons = [...document.querySelectorAll('[data-hero-slide]')];
  const pauseButton = document.querySelector('#hero-pause');
  const heroSlides = [
    {
      main: ['assets/founder-lex.webp', 'Lucci Luciano on set in her studio, camera in hand'],
      top: ['assets/on-set.webp', 'Lucci Media founder on set with a creative brief'],
      detail: ['assets/behind-the-lens.webp', 'A close view of a camera at work during a beauty shoot'],
      caption: 'Lucci · behind the lens',
      title: 'Campaign set 1 of 3',
    },
    {
      main: ['assets/studio-story.webp', 'Lucci on set at the studio, camera in hand'],
      top: ['assets/on-set.webp', 'A Lucci Media creative set in the studio'],
      detail: ['assets/behind-the-lens.webp', 'A close view of a camera at work during a beauty shoot'],
      caption: 'The studio · Boston',
      title: 'Campaign set 2 of 3',
    },
    {
      main: ['assets/brown-sugar-skin.webp', 'Brown Sugar Skin brand portrait from a client rebrand'],
      top: ['assets/product-content.webp', 'Carefully styled product and accessories for a content shoot'],
      detail: ['assets/hero-portrait.webp', 'Beauty portrait photographed for a Lucci Media client'],
      caption: 'Brown Sugar Skin · Branding',
      title: 'Campaign set 3 of 3',
    },
  ];
  let currentSlide = 0;
  let slideshowPaused = reducedMotion;
  let slideshowTimer;
  let slideTransitionTimer;

  const setSlide = (index, animate = true) => {
    const nextIndex = (index + heroSlides.length) % heroSlides.length;
    const slide = heroSlides[nextIndex];
    currentSlide = nextIndex;
    clearTimeout(slideTransitionTimer);

    slideButtons.forEach((button, buttonIndex) => {
      const selected = buttonIndex === currentSlide;
      button.classList.toggle('is-current', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    if (heroIndex) heroIndex.textContent = `LM — ${String(currentSlide + 1).padStart(2, '0')} / 03`;
    if (heroStatus) heroStatus.textContent = slide.title;

    const updateImages = () => {
      [[heroMain, slide.main], [heroTop, slide.top], [heroDetail, slide.detail]].forEach(([image, data]) => {
        if (!image || !data) return;
        image.src = data[0];
        image.alt = data[1];
      });
      if (heroCaption) heroCaption.textContent = slide.caption;
      requestAnimationFrame(() => heroVisual?.classList.remove('is-changing'));
    };

    if (!animate || reducedMotion || !heroVisual) {
      heroVisual?.classList.remove('is-changing');
      updateImages();
      return;
    }
    heroVisual.classList.add('is-changing');
    slideTransitionTimer = window.setTimeout(updateImages, 430);
  };

  const updateSlideshowTimer = () => {
    clearInterval(slideshowTimer);
    if (!pauseButton) return;
    const shouldPause = slideshowPaused || document.hidden;
    pauseButton.textContent = shouldPause ? 'Play' : 'Pause';
    pauseButton.setAttribute('aria-label', shouldPause ? 'Play campaign slideshow' : 'Pause campaign slideshow');
    if (!shouldPause) slideshowTimer = window.setInterval(() => setSlide(currentSlide + 1), 7200);
  };

  slideButtons.forEach((button) => button.addEventListener('click', () => {
    setSlide(Number(button.dataset.heroSlide));
    updateSlideshowTimer();
  }));
  pauseButton?.addEventListener('click', () => {
    slideshowPaused = !slideshowPaused;
    updateSlideshowTimer();
  });
  document.addEventListener('visibilitychange', updateSlideshowTimer);
  heroSlides.flatMap((slide) => [slide.main[0], slide.top[0], slide.detail[0]]).forEach((src) => {
    const image = new Image();
    image.src = src;
  });
  updateSlideshowTimer();

  const serviceItems = [...document.querySelectorAll('.service-item')];
  serviceItems.forEach((item) => {
    const trigger = item.querySelector('.service-trigger');
    const panel = item.querySelector('.service-panel');
    trigger?.addEventListener('click', () => {
      const shouldOpen = trigger.getAttribute('aria-expanded') !== 'true';
      serviceItems.forEach((otherItem) => {
        if (otherItem === item) return;
        const otherButton = otherItem.querySelector('.service-trigger');
        const otherPanel = otherItem.querySelector('.service-panel');
        otherItem.classList.remove('is-open');
        otherButton?.setAttribute('aria-expanded', 'false');
        if (otherPanel) window.setTimeout(() => {
          if (otherButton?.getAttribute('aria-expanded') === 'false') otherPanel.hidden = true;
        }, 280);
      });

      trigger.setAttribute('aria-expanded', String(shouldOpen));
      if (shouldOpen) {
        if (panel) {
          panel.hidden = false;
          requestAnimationFrame(() => item.classList.add('is-open'));
        }
      } else {
        item.classList.remove('is-open');
        if (panel) window.setTimeout(() => {
          if (trigger.getAttribute('aria-expanded') === 'false') panel.hidden = true;
        }, 280);
      }
    });
  });

  const serviceList = document.querySelector('#service-list');
  const serviceStatus = document.querySelector('#service-carousel-status');
  const servicePrev = document.querySelector('[data-service-prev]');
  const serviceNext = document.querySelector('[data-service-next]');
  let activeService = 0;
  let serviceScrollFrame = 0;
  const updateServiceCarousel = () => {
    if (!serviceList || !serviceItems.length) return;
    const leadingEdge = serviceList.getBoundingClientRect().left;
    activeService = serviceItems.reduce((closest, item, index) => {
      const bounds = item.getBoundingClientRect();
      const distance = Math.abs(bounds.left - leadingEdge);
      const closestBounds = serviceItems[closest].getBoundingClientRect();
      return distance < Math.abs(closestBounds.left - leadingEdge) ? index : closest;
    }, 0);
    if (serviceStatus) serviceStatus.textContent = `${String(activeService + 1).padStart(2, '0')} / ${String(serviceItems.length).padStart(2, '0')}`;
    if (servicePrev) servicePrev.disabled = activeService === 0;
    if (serviceNext) serviceNext.disabled = activeService === serviceItems.length - 1;
  };
  const scrollService = (direction) => {
    const next = Math.min(serviceItems.length - 1, Math.max(0, activeService + direction));
    serviceItems[next]?.scrollIntoView({ behavior: reducedMotion ? 'instant' : 'smooth', block: 'nearest', inline: 'start' });
  };
  servicePrev?.addEventListener('click', () => scrollService(-1));
  serviceNext?.addEventListener('click', () => scrollService(1));
  serviceList?.addEventListener('scroll', () => {
    if (serviceScrollFrame) return;
    serviceScrollFrame = requestAnimationFrame(() => {
      serviceScrollFrame = 0;
      updateServiceCarousel();
    });
  }, { passive: true });
  window.addEventListener('resize', updateServiceCarousel);
  updateServiceCarousel();

  const quoteSlides = [...document.querySelectorAll('[data-quote-slide]')];
  const quoteDots = [...document.querySelectorAll('[data-quote-dot]')];
  const quoteStatus = document.querySelector('#quote-status');
  let activeQuote = 0;
  const setQuote = (index) => {
    if (!quoteSlides.length) return;
    activeQuote = (index + quoteSlides.length) % quoteSlides.length;
    quoteSlides.forEach((slide, slideIndex) => {
      const selected = slideIndex === activeQuote;
      slide.hidden = !selected;
      slide.classList.toggle('is-active', selected);
    });
    quoteDots.forEach((dot, dotIndex) => {
      const selected = dotIndex === activeQuote;
      dot.classList.toggle('is-active', selected);
      dot.setAttribute('aria-selected', String(selected));
    });
    if (quoteStatus) {
      quoteStatus.textContent = `.${String(activeQuote + 1).padStart(2, '0')}/${quoteSlides.length}`;
    }
  };

  quoteDots.forEach((dot, dotIndex) => {
    dot.addEventListener('click', () => {
      setQuote(dotIndex);
      startQuoteTimer();
    });
  });

  document.querySelector('[data-quote-prev]')?.addEventListener('click', () => {
    setQuote(activeQuote - 1);
    startQuoteTimer();
  });
  document.querySelector('[data-quote-next]')?.addEventListener('click', () => {
    setQuote(activeQuote + 1);
    startQuoteTimer();
  });

  // Testimonials Auto-Cycle with Smooth Transition & Hover Pause
  let quoteTimer = null;
  const startQuoteTimer = () => {
    if (quoteTimer) clearInterval(quoteTimer);
    quoteTimer = setInterval(() => {
      setQuote(activeQuote + 1);
    }, 6000);
  };
  startQuoteTimer();

  const testimonialsContainer = document.querySelector('.tsa-testimonials-container');
  testimonialsContainer?.addEventListener('mouseenter', () => clearInterval(quoteTimer));
  testimonialsContainer?.addEventListener('mouseleave', () => startQuoteTimer());

  // Archive continuous marquee controls
  const archivePauseToggle = document.querySelector('#archive-pause-toggle');
  const archiveTracks = document.querySelectorAll('.archive-track');
  archivePauseToggle?.addEventListener('click', () => {
    const isPaused = archivePauseToggle.getAttribute('aria-pressed') !== 'true';
    archivePauseToggle.setAttribute('aria-pressed', String(isPaused));
    const pauseText = archivePauseToggle.querySelector('.pause-text');
    const pauseIcon = archivePauseToggle.querySelector('.pause-icon');
    if (pauseText) pauseText.textContent = isPaused ? 'Play' : 'Pause';
    if (pauseIcon) pauseIcon.textContent = isPaused ? '▶' : '⏸';
    archiveTracks.forEach(t => t.classList.toggle('is-paused', isPaused));
  });

  const legacyMarqueeTrack = document.querySelector('#photo-marquee-track');
  const legacyMarqueeToggle = document.querySelector('#photo-marquee-toggle');
  legacyMarqueeToggle?.addEventListener('click', () => {
    const paused = legacyMarqueeToggle.getAttribute('aria-pressed') !== 'true';
    legacyMarqueeToggle.setAttribute('aria-pressed', String(paused));
    legacyMarqueeToggle.textContent = paused ? 'Play gallery' : 'Pause gallery';
    legacyMarqueeTrack?.classList.toggle('is-paused', paused);
  });

  const counters = [...document.querySelectorAll('[data-count]')];
  if (counters.length && 'IntersectionObserver' in window && !reducedMotion) {
    const countObserver = new IntersectionObserver((entries, observer) => {
      entries.filter((entry) => entry.isIntersecting).forEach((entry) => {
        const counter = entry.target;
        observer.unobserve(counter);
        const target = Number(counter.dataset.countValue || counter.textContent);
        const startedAt = performance.now();
        counter.textContent = '0';
        const tick = (now) => {
          const progress = Math.min(1, (now - startedAt) / 1350);
          const eased = 1 - Math.pow(1 - progress, 3);
          counter.textContent = String(Math.round(target * eased));
          if (progress < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: .65 });
    counters.forEach((counter) => countObserver.observe(counter));
  }

  const parallaxImages = [...document.querySelectorAll('[data-parallax]')];
  // Gentle, calm parallax distance so imagery glides gracefully without rushing
  const parallaxDistance = window.matchMedia('(pointer: coarse)').matches ? 8 : 18;
  const visibleParallax = new Set();
  if ('IntersectionObserver' in window) {
    const parallaxObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) visibleParallax.add(entry.target);
        else visibleParallax.delete(entry.target);
      });
    }, { rootMargin: '100px 0px' });
    parallaxImages.forEach((image) => parallaxObserver.observe(image));
  } else {
    parallaxImages.forEach((image) => visibleParallax.add(image));
  }

  // Dynamic chapter tracker elements
  const chapterHud = document.getElementById('chapter-hud');
  const hudText = chapterHud?.querySelector('.hud-text');
  let currentChapter = '';

  const trackedSections = [
    { id: 'hero', label: '[ 01 HOME ]' },
    { id: 'archive', label: '[ 02 ARCHIVE ]' },
    { id: 'what-we-do', label: '[ 03 WHAT WE DO ]' },
    { id: 'services', label: '[ 04 SERVICES ]' },
    { id: 'studio', label: '[ 05 STUDIO ]' },
    { id: 'city-showcase', label: '[ 06 BOSTON ]' },
    { id: 'love', label: '[ 07 CLIENT LOVE ]' },
    { id: 'contact', label: '[ 08 APPLY ]' }
  ];

  let scrollFrame = 0;
  const updateScrollEffects = () => {
    scrollFrame = 0;
    const scrollTop = window.scrollY;
    const scrollRange = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const height = window.innerHeight;

    header?.classList.toggle('is-scrolled', scrollTop > 18);
    progress?.style.setProperty('transform', `scaleX(${Math.min(1, Math.max(0, scrollTop / scrollRange))})`);

    // Section Chapter Tracker HUD
    let activeSec = null;
    const checkLine = height * 0.45;
    for (const sec of trackedSections) {
      const el = document.getElementById(sec.id);
      if (el) {
        const r = el.getBoundingClientRect();
        if (r.top <= checkLine && r.bottom > checkLine) {
          activeSec = sec;
          break;
        }
      }
    }
    if (activeSec && activeSec.label !== currentChapter) {
      currentChapter = activeSec.label;
      if (hudText) hudText.textContent = currentChapter;
      chapterHud?.classList.add('is-visible');
    } else if (!activeSec && scrollTop < 100) {
      chapterHud?.classList.remove('is-visible');
    }

    if (!reducedMotion) {
      // 1. Hero Fixed Background Zoom & Content Drift (Subtle & Calm)
      const hero = document.querySelector('.hero');
      const heroBgImg = document.querySelector('.hero-bg-img');
      const heroCopy = document.querySelector('.hero-copy');
      const heroVisualElement = document.querySelector('.hero-visual');
      const heroRect = hero?.getBoundingClientRect();
      if (heroRect && heroRect.bottom > 0 && heroRect.top < height) {
        const progressThroughHero = Math.min(1, Math.max(0, -heroRect.top / Math.max(heroRect.height, 1)));
        const heroScale = 1.01 + progressThroughHero * 0.035;
        heroBgImg?.style.setProperty('--hero-scale', heroScale.toFixed(3));
        heroCopy?.style.setProperty('--scroll-copy-y', `${-progressThroughHero * 8}px`);
        heroCopy?.style.setProperty('--scroll-copy-opacity', String(1 - progressThroughHero * .1));
        heroVisualElement?.style.setProperty('--scroll-visual-y', `${progressThroughHero * 10}px`);
      }

      // 2. Studio Section Gentle Parallax
      const studioSec = document.getElementById('studio');
      const behindMiddle = document.querySelector('.tsa-behind-middle');
      const behindRight = document.querySelector('.tsa-behind-right');
      if (studioSec && (behindMiddle || behindRight)) {
        const studioRect = studioSec.getBoundingClientRect();
        if (studioRect.bottom > 0 && studioRect.top < height) {
          const centerOffset = (height / 2 - (studioRect.top + studioRect.height / 2)) / (height / 2 + studioRect.height / 2);
          const middleOffset = centerOffset * 18;
          const portraitOffset = centerOffset * -12;
          behindMiddle?.style.setProperty('--middle-y', `${middleOffset.toFixed(1)}px`);
          behindRight?.style.setProperty('--portrait-y', `${portraitOffset.toFixed(1)}px`);
        }
      }

      // 3. City Section: Subtle Background Zoom + Soft Polaroid Parallax
      const citySec = document.getElementById('city-showcase');
      const cityBgImg = document.querySelector('.city-bg-img');
      const cityPolaroid = document.getElementById('city-polaroid');
      if (citySec) {
        const cityRect = citySec.getBoundingClientRect();
        if (cityRect.bottom > 0 && cityRect.top < height) {
          const cityProgress = Math.min(1, Math.max(0, (height - cityRect.top) / (height + cityRect.height)));
          const cityScale = 1.01 + cityProgress * 0.04;
          cityBgImg?.style.setProperty('--city-scale', cityScale.toFixed(3));
          const polaroidOffset = (0.5 - cityProgress) * 22;
          cityPolaroid?.style.setProperty('--polaroid-y', `${polaroidOffset.toFixed(1)}px`);
        }
      }

      // 4. CTA Panoramic Banner Subtle Zoom
      const bannerFrame = document.querySelector('.tsa-cta-banner-frame');
      const bannerImg = document.querySelector('.tsa-cta-banner-media img');
      if (bannerFrame && bannerImg) {
        const bannerRect = bannerFrame.getBoundingClientRect();
        if (bannerRect.bottom > 0 && bannerRect.top < height) {
          const bannerProgress = Math.min(1, Math.max(0, (height - bannerRect.top) / (height + bannerRect.height)));
          const bannerScale = 1.01 + bannerProgress * 0.04;
          bannerImg.style.setProperty('--banner-scale', bannerScale.toFixed(3));
        }
      }

      // 5. Contact Decorative Flower Subtle Scroll Rotation
      const contactSec = document.getElementById('contact');
      const contactFlower = document.querySelector('.contact-flower');
      if (contactSec && contactFlower) {
        const cRect = contactSec.getBoundingClientRect();
        if (cRect.top < height && cRect.bottom > 0) {
          const cProgress = (height - cRect.top) / (height + cRect.height);
          contactFlower.style.setProperty('--flower-rot', `${(14 + cProgress * 72).toFixed(1)}deg`);
        }
      }

      // 6. Footer Giant Wordmark Kinetic Opposing Drift
      const footerSec = document.getElementById('footer');
      if (footerSec) {
        const footerRect = footerSec.getBoundingClientRect();
        if (footerRect.top < height && footerRect.bottom > 0) {
          const fProgress = Math.min(1, Math.max(0, (height - footerRect.top) / (height + footerRect.height)));
          const drift = (fProgress - 0.5) * 44; // smooth opposing slide
          footerSec.style.setProperty('--wordmark-drift-left', `${(-drift).toFixed(1)}px`);
          footerSec.style.setProperty('--wordmark-drift-right', `${drift.toFixed(1)}px`);
        }
      }

      // 7. Standard Parallax Elements (Soft & Gentle)
      visibleParallax.forEach((image) => {
        const rect = image.getBoundingClientRect();
        const centerOffset = (height / 2 - (rect.top + rect.height / 2)) / (height / 2 + rect.height / 2);
        const offset = Math.max(-1.2, Math.min(1.2, centerOffset)) * parallaxDistance;
        image.style.setProperty('--parallax-y', `${offset.toFixed(1)}px`);
      });
    }
  };
  const scheduleScrollEffects = () => {
    if (scrollFrame) return;
    scrollFrame = window.requestAnimationFrame(updateScrollEffects);
  };
  window.addEventListener('scroll', scheduleScrollEffects, { passive: true });
  window.addEventListener('resize', scheduleScrollEffects);
  if (lenis) {
    lenis.on('scroll', scheduleScrollEffects);
  }
  updateScrollEffects();

  // Smooth scroll for internal anchor links using Lenis
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const targetId = anchor.getAttribute('href');
      if (!targetId || targetId === '#') return;
      if (targetId === '#top') {
        e.preventDefault();
        if (lenis) lenis.scrollTo(0, { duration: 1.2 });
        else window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }
      const targetElem = document.querySelector(targetId);
      if (targetElem) {
        e.preventDefault();
        if (lenis) {
          lenis.scrollTo(targetElem, { offset: -70, duration: 1.2 });
        } else {
          targetElem.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });

  if (window.matchMedia('(pointer: fine)').matches && !reducedMotion) {
    heroVisual?.addEventListener('pointermove', (event) => {
      if (event.pointerType !== 'mouse') return;
      const bounds = heroVisual.getBoundingClientRect();
      const x = (event.clientX - bounds.left - bounds.width / 2) / (bounds.width / 2);
      const y = (event.clientY - bounds.top - bounds.height / 2) / (bounds.height / 2);
      heroVisual.querySelectorAll('.hero-shot').forEach((shot, index) => {
        const strength = [7, 12, 17][index] || 7;
        shot.style.setProperty('--cursor-x', `${(x * strength).toFixed(1)}px`);
        shot.style.setProperty('--cursor-y', `${(y * strength).toFixed(1)}px`);
      });
    });
    heroVisual?.addEventListener('pointerleave', () => {
      heroVisual.querySelectorAll('.hero-shot').forEach((shot) => {
        shot.style.removeProperty('--cursor-x');
        shot.style.removeProperty('--cursor-y');
      });
    });

    document.querySelectorAll('.work-card').forEach((card) => {
      const media = card.querySelector('.work-image');
      media?.addEventListener('pointermove', (event) => {
        if (event.pointerType !== 'mouse') return;
        const bounds = media.getBoundingClientRect();
        const x = (event.clientX - bounds.left) / bounds.width - .5;
        const y = (event.clientY - bounds.top) / bounds.height - .5;
        media.style.setProperty('--tilt-x', `${(-y * 3.2).toFixed(2)}deg`);
        media.style.setProperty('--tilt-y', `${(x * 3.2).toFixed(2)}deg`);
      });
      media?.addEventListener('pointerleave', () => {
        media.style.removeProperty('--tilt-x');
        media.style.removeProperty('--tilt-y');
      });
    });

    document.querySelectorAll('.button, .header-cta').forEach((control) => {
      control.addEventListener('pointermove', (event) => {
        if (event.pointerType !== 'mouse') return;
        const bounds = control.getBoundingClientRect();
        const x = (event.clientX - bounds.left - bounds.width / 2) * .055;
        const y = (event.clientY - bounds.top - bounds.height / 2) * .09;
        control.style.translate = `${x.toFixed(1)}px ${y.toFixed(1)}px`;
      });
      control.addEventListener('pointerleave', () => { control.style.translate = ''; });
    });
  }

  /* ==========================================================================
     OUR CITY. YOUR CONTENT. - POLAROID AUTO-CYCLE ANIMATION
     ========================================================================== */
  const polaroidFrame = document.getElementById('city-polaroid');
  const citySlides = polaroidFrame ? [...polaroidFrame.querySelectorAll('[data-city-slide]')] : [];
  if (polaroidFrame && citySlides.length > 1) {
    let currentCityIdx = 0;
    let cityTimer = null;
    let isCityPaused = false;

    const showCitySlide = (index) => {
      citySlides.forEach((slide, i) => {
        slide.classList.toggle('is-active', i === index);
      });
      currentCityIdx = index;
    };

    const nextCitySlide = () => {
      if (isCityPaused) return;
      const nextIdx = (currentCityIdx + 1) % citySlides.length;
      showCitySlide(nextIdx);
    };

    const startCityCycle = () => {
      if (cityTimer) clearInterval(cityTimer);
      cityTimer = setInterval(nextCitySlide, 2400);
    };

    polaroidFrame.addEventListener('mouseenter', () => { isCityPaused = true; });
    polaroidFrame.addEventListener('pointermove', (e) => {
      if (e.pointerType !== 'mouse') return;
      const rect = polaroidFrame.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      polaroidFrame.style.setProperty('--tilt-rx', `${(-y * 12).toFixed(1)}deg`);
      polaroidFrame.style.setProperty('--tilt-ry', `${(x * 12).toFixed(1)}deg`);
    });
    polaroidFrame.addEventListener('pointerleave', () => {
      isCityPaused = false;
      polaroidFrame.style.removeProperty('--tilt-rx');
      polaroidFrame.style.removeProperty('--tilt-ry');
    });
    polaroidFrame.addEventListener('click', () => {
      const nextIdx = (currentCityIdx + 1) % citySlides.length;
      showCitySlide(nextIdx);
    });

    startCityCycle();
  }

  // --- "THE WORK SPEAKS" NUMBER COUNT-UP ANIMATION ---
  const workSpeaksSection = document.querySelector('#the-work-speaks');
  if (workSpeaksSection) {
    const statNums = workSpeaksSection.querySelectorAll('.work-speaks-stat .work-speaks-num');

    // Expected 7 stats:
    // 0: Revenue Growth (0 -> 467%)
    // 1: In Production ($0 -> $1M+)
    // 2: From One Campaign ($0 -> $84K)
    // 3: Monthly Revenue Lift (0 -> 64%)
    // 4: Year Over Year Growth (0 -> 34%)
    // 5: Recurring Membership Growth (0 -> 189%)
    // 6: Revenue From Trainings (Static: 2X - preserved as-is)
    if (statNums.length >= 6) {
      const statsToAnimate = [
        {
          el: statNums[0],
          startText: '0',
          finalText: '467%',
          target: 467,
          format: (val) => `${val}%`
        },
        {
          el: statNums[1],
          startText: '$0',
          finalText: '$1M+',
          target: 1,
          format: (val) => (val >= 1 ? '$1M+' : '$0')
        },
        {
          el: statNums[2],
          startText: '$0',
          finalText: '$84K',
          target: 84,
          format: (val) => (val === 0 ? '$0' : `$${val}K`)
        },
        {
          el: statNums[3],
          startText: '0',
          finalText: '64%',
          target: 64,
          format: (val) => `${val}%`
        },
        {
          el: statNums[4],
          startText: '0',
          finalText: '34%',
          target: 34,
          format: (val) => `${val}%`
        },
        {
          el: statNums[5],
          startText: '0',
          finalText: '189%',
          target: 189,
          format: (val) => `${val}%`
        }
      ];

      // Respect prefers-reduced-motion: if enabled, keep final values visible without animating
      if (!reducedMotion) {
        // Set initial starting values on page load
        statsToAnimate.forEach((item) => {
          item.el.textContent = item.startText;
        });

        let hasAnimated = false;
        const duration = 2200; // 2.2 seconds duration (within 2 - 2.5s)

        const startCountUp = () => {
          if (hasAnimated) return;
          hasAnimated = true;

          const startTime = performance.now();

          const updateCounter = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(1, elapsed / duration);
            // Ease-out cubic: smooth progressive counting that decelerates gracefully
            const eased = 1 - Math.pow(1 - progress, 3);

            statsToAnimate.forEach((item) => {
              if (progress >= 1) {
                item.el.textContent = item.finalText;
              } else {
                const current = Math.round(item.target * eased);
                item.el.textContent = item.format(current);
              }
            });

            if (progress < 1) {
              requestAnimationFrame(updateCounter);
            } else {
              // Ensure exact final values and formatting on completion
              statsToAnimate.forEach((item) => {
                item.el.textContent = item.finalText;
              });
            }
          };

          requestAnimationFrame(updateCounter);
        };

        if ('IntersectionObserver' in window) {
          const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
              if (entry.isIntersecting && !hasAnimated) {
                observer.unobserve(workSpeaksSection);
                observer.disconnect();
                startCountUp();
              }
            });
          }, {
            threshold: 0.25,
            rootMargin: '0px 0px -40px 0px'
          });

          observer.observe(workSpeaksSection);
        } else {
          // Fallback if IntersectionObserver is not available
          startCountUp();
        }
      }
    }
  }

  const year = document.querySelector('#year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
