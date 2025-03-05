document.addEventListener('DOMContentLoaded', function() {
    // ===== INITIALIZE ANIMATIONS =====
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        mirror: false
    });
    
    // ===== NAVIGATION =====
    // Header scroll effect
    const header = document.querySelector('header');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    
    // Mobile menu toggle
    const mobileMenuBtn = document.querySelector('[data-collapse-toggle="mobile-menu"]');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }
    
    // Close mobile menu when clicking on a link
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');
    mobileLinks.forEach(link => {
        link.addEventListener('click', function() {
            mobileMenu.classList.add('hidden');
        });
    });
    
    // Smooth scrolling for all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80, // Adjust for header height
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // ===== CATEGORY SWITCHER =====
    const categoryItems = document.querySelectorAll('.category-item');
    const carouselCategories = document.querySelectorAll('.carousel-category');
    
    categoryItems.forEach(item => {
        item.addEventListener('click', function() {
            // Update active class for category items
            categoryItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');
            
            // Get the selected category
            const category = this.getAttribute('data-category');
            
            // Hide all categories and show the selected one
            carouselCategories.forEach(cat => {
                cat.classList.add('hidden');
                if (cat.id === category) {
                    cat.classList.remove('hidden');
                    cat.classList.add('active');
                    // Reset carousel position
                    const container = cat.querySelector('.carousel-container');
                    if (container) {
                        container.style.transform = 'translateX(0)';
                    }
                }
            });
            
            // Initialize dots for the current category
            initCarouselDots(category);
        });
    });
    
    // ===== CAROUSEL =====
    function initCarouselDots(categoryId) {
        const category = document.getElementById(categoryId);
        if (!category) return;
        
        const carouselContainer = category.querySelector('.carousel-container');
        const carouselItems = category.querySelectorAll('.carousel-item');
        const dotsContainer = document.querySelector('.carousel-dots');
        
        if (!carouselContainer || !dotsContainer) return;
        
        // Calculate number of pages (3 items per page on desktop, 1 on mobile)
        const itemsPerPage = window.innerWidth >= 768 ? 3 : 1;
        const pageCount = Math.ceil(carouselItems.length / itemsPerPage);
        
        // Create dots
        dotsContainer.innerHTML = '';
        for (let i = 0; i < pageCount; i++) {
            const dot = document.createElement('div');
            dot.classList.add('carousel-dot');
            if (i === 0) dot.classList.add('active');
            dot.dataset.index = i;
            dot.addEventListener('click', () => {
                moveCarousel(categoryId, i);
                updateActiveDot(i);
            });
            dotsContainer.appendChild(dot);
        }
    }
    
    function moveCarousel(categoryId, index) {
        const category = document.getElementById(categoryId);
        const carouselContainer = category.querySelector('.carousel-container');
        const itemsPerPage = window.innerWidth >= 768 ? 3 : 1;
        const slidePercentage = -(index * (100 / itemsPerPage));
        carouselContainer.style.transform = `translateX(${slidePercentage}%)`;
    }
    
    function updateActiveDot(index) {
        const dots = document.querySelectorAll('.carousel-dot');
        dots.forEach(dot => {
            dot.classList.remove('active');
            if (parseInt(dot.dataset.index) === index) {
                dot.classList.add('active');
            }
        });
    }
    
    // Auto-scroll carousel
    function autoScrollCarousel() {
        const activeCategory = document.querySelector('.carousel-category.active');
        if (!activeCategory) return;
        
        const categoryId = activeCategory.id;
        const dots = document.querySelectorAll('.carousel-dot');
        if (dots.length === 0) return;
        
        let activeIndex = 0;
        dots.forEach((dot, index) => {
            if (dot.classList.contains('active')) {
                activeIndex = index;
            }
        });
        
        // Move to next dot
        activeIndex = (activeIndex + 1) % dots.length;
        moveCarousel(categoryId, activeIndex);
        updateActiveDot(activeIndex);
    }
    
    // Initialize carousel for default category
    initCarouselDots('wedding');
    
    // Set auto-scroll interval
    const autoScrollInterval = setInterval(autoScrollCarousel, 5000);
    
    // Pause auto-scroll on carousel hover
    const carouselWrapper = document.querySelector('.carousel-wrapper');
    if (carouselWrapper) {
        carouselWrapper.addEventListener('mouseenter', () => {
            clearInterval(autoScrollInterval);
        });
        
        carouselWrapper.addEventListener('mouseleave', () => {
            setInterval(autoScrollCarousel, 5000);
        });
    }
    
    // Handle window resize for responsive carousel
    window.addEventListener('resize', () => {
        const activeCategory = document.querySelector('.carousel-category.active');
        if (activeCategory) {
            initCarouselDots(activeCategory.id);
        }
    });
    
    // ===== FORM VALIDATION =====
    const bookingForm = document.getElementById('booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Basic form validation
            let isValid = true;
            const formInputs = this.querySelectorAll('input[required], select[required]');
            
            formInputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('border-red-500');
                } else {
                    input.classList.remove('border-red-500');
                }
            });
            
            // Email validation
            const emailInput = this.querySelector('#email');
            if (emailInput && emailInput.value) {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailPattern.test(emailInput.value)) {
                    isValid = false;
                    emailInput.classList.add('border-red-500');
                }
            }
            
            // Phone validation
            const phoneInput = this.querySelector('#phone');
            if (phoneInput && phoneInput.value) {
                const phonePattern = /^[\d\+\-\(\)\s]+$/;
                if (!phonePattern.test(phoneInput.value)) {
                    isValid = false;
                    phoneInput.classList.add('border-red-500');
                }
            }
            
            if (isValid) {
                // Show success message (in real implementation, would send data to server)
                showFormMessage('Your booking request has been submitted successfully! We will contact you soon.', 'success');
                bookingForm.reset();
            } else {
                showFormMessage('Please fill all required fields correctly.', 'error');
            }
        });
        
        // Input validation on change
        const formInputs = bookingForm.querySelectorAll('input, select, textarea');
        formInputs.forEach(input => {
            input.addEventListener('input', function() {
                if (this.hasAttribute('required') && this.value.trim()) {
                    this.classList.remove('border-red-500');
                }
                
                // Live email validation
                if (this.id === 'email' && this.value) {
                    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (emailPattern.test(this.value)) {
                        this.classList.remove('border-red-500');
                    }
                }
                
                // Live phone validation
                if (this.id === 'phone' && this.value) {
                    const phonePattern = /^[\d\+\-\(\)\s]+$/;
                    if (phonePattern.test(this.value)) {
                        this.classList.remove('border-red-500');
                    }
                }
            });
        });
    }
    
    // Show form message
    function showFormMessage(message, type) {
        const formContainer = document.querySelector('#booking-form').parentNode;
        
        // Remove existing message
        const existingMessage = formContainer.querySelector('.form-message');
        if (existingMessage) {
            existingMessage.remove();
        }
        
        // Create message element
        const messageElement = document.createElement('div');
        messageElement.classList.add('form-message', 'p-4', 'rounded-lg', 'mt-4');
        
        if (type === 'success') {
            messageElement.classList.add('bg-green-100', 'text-green-800');
        } else {
            messageElement.classList.add('bg-red-100', 'text-red-800');
        }
        
        messageElement.textContent = message;
        
        // Add to form container
        formContainer.appendChild(messageElement);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            messageElement.classList.add('opacity-0');
            setTimeout(() => {
                messageElement.remove();
            }, 300);
        }, 5000);
    }
    
    // ===== ANIMATIONS =====
    // Animate elements when they enter viewport
    const animatedElements = document.querySelectorAll('.animate-on-load');
    
    function checkInView() {
        animatedElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                if (element.classList.contains('animate-fade-in')) {
                    element.style.animation = 'fadeIn 1s forwards';
                } else if (element.classList.contains('animate-slide-up')) {
                    element.style.animation = 'slideUp 1s forwards';
                } else if (element.classList.contains('animate-slide-in-right')) {
                    element.style.animation = 'slideInRight 1s forwards';
                } else if (element.classList.contains('animate-slide-in-left')) {
                    element.style.animation = 'slideInLeft 1s forwards';
                } else {
                    element.style.animation = 'fadeIn 1s forwards';
                }
            }
        });
    }
    
    window.addEventListener('scroll', checkInView);
    window.addEventListener('load', checkInView);
    
    // Image hover effects
    const hoverImages = document.querySelectorAll('.image-hover');
    hoverImages.forEach(image => {
        const img = image.querySelector('img');
        if (img) {
            img.addEventListener('mouseenter', () => {
                img.style.transform = 'scale(1.1)';
            });
            
            img.addEventListener('mouseleave', () => {
                img.style.transform = 'scale(1)';
            });
        }
    });
    
    // ===== PAGE LOADING =====
    // Hide loading spinner when page is fully loaded
    window.addEventListener('load', () => {
        const loader = document.querySelector('.loading');
        if (loader) {
            loader.classList.add('loaded');
            setTimeout(() => {
                loader.style.display = 'none';
            }, 500);
        }
    });
});