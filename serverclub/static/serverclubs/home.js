// Particle Background
    const canvas = document.getElementById('particle-canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particlesArray;

    class Particle {
      constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 5 + 1; // Random size between 1 and 6
        this.speedX = Math.random() * 3 - 1.5; // Random speed
        this.speedY = Math.random() * 3 - 1.5; // Random speed
      }

      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        // Bounce off edges
        if (this.size > 0) {
          if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
          if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
        }
      }

      draw() {
        ctx.fillStyle = 'rgba(0, 255, 204, 0.8)'; // Soft glow color
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.closePath();
        ctx.fill();
      }
    }

    function init() {
      particlesArray = [];
      for (let i = 0; i < 100; i++) {
        particlesArray.push(new Particle());
      }
    }

    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particlesArray.forEach((particle) => {
        particle.update();
        particle.draw();
      });
      requestAnimationFrame(animate);
    }

    window.addEventListener('resize', () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      init();
    });

    init();
    animate();

    // Loading overlay logic
    const loadingOverlay = document.getElementById('loadingOverlay');

    // Show loading overlay when the Join button is pressed
    const joinButton = document.querySelector('.join-btn');
    joinButton.addEventListener('click', (e) => {
      loadingOverlay.classList.add('visible');

      // Prevent default action (if it's a link)
      e.preventDefault();

      // Simulate loading for demonstration (remove this in production)
      setTimeout(() => {
        // Redirect or continue with form submission here if needed
        window.location.href = joinButton.href; // Navigate to the URL of the button
      }, 1000); // Adjust the time as necessary for your application's loading state
    });

    // Hide loading overlay when the page has finished loading
    window.addEventListener('load', () => {
      loadingOverlay.classList.remove('visible');
    });
