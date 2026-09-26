document.addEventListener("DOMContentLoaded", function() {
    // Define the sequence of pages
    const pages = [
        //'/',
        '/',
        '/run-expectancy',
        '/batting_average',
        '/offensive-stats',
        '/pitching-stats',
        '/fastball-velocity',
        
        '/payroll-wins',
        '/knowledge-base',
        '/contact'
        // Add other routes here as needed
    ];

     // Get the current page URL path and remove the base path
    const basePath = '/baseball-viz';
    let currentPath = window.location.pathname;
    if (currentPath.startsWith(basePath)) {
        currentPath = currentPath.substring(basePath.length);
    }
    console.log("Current Path:", currentPath);

    // Find the index of the current page
    const currentIndex = pages.indexOf(currentPath);
    console.log("Current Index:", currentIndex);

    // Get the navigation buttons
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");
 
     /// Set the href for the previous button
    if (currentIndex > 0) {
        prevButton.href = basePath + pages[currentIndex - 1];
    } else {
        prevButton.style.display = "none"; // Hide if there's no previous page
    }

    // Set the href for the next button
    if (currentIndex < pages.length - 1 && currentIndex !== -1) {
        nextButton.href = basePath + pages[currentIndex + 1];
    } else {
        nextButton.style.display = "none"; // Hide if there's no next page
    }
 });

 //set scroll top button. appears when users scroll down
 const scrollToTopBtn = document.getElementById('scrollToTopBtn');

 window.addEventListener('scroll', () => {
     if (window.scrollY > 300) {
         scrollToTopBtn.style.display = 'block';
     } else {
         scrollToTopBtn.style.display = 'none';
     }
 });
 
 scrollToTopBtn.addEventListener('click', () => {
     window.scrollTo({
         top: 0,
         behavior: 'smooth'
     });
 });

 //defer loading of iframes until they are in the viewport to improve initial load performance
 document.addEventListener('DOMContentLoaded', function() {
    const lazyIframes = document.querySelectorAll('iframe.lazy-load');
    const iframeObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const iframe = entry.target;
                iframe.src = iframe.dataset.src;
                iframe.classList.remove('lazy-load');
                observer.unobserve(iframe);
            }
        });
    });

    lazyIframes.forEach(iframe => {
        iframeObserver.observe(iframe);
    });
});


