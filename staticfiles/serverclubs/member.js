  // Show loading overlay on page load
    window.onload = function() {
        document.getElementById('loading-overlay').style.display = 'none'; // Hide loading overlay when page loads
    };

    // Show loading overlay when making AJAX requests (example)
    function showLoading() {
        document.getElementById('loading-overlay').style.display = 'flex'; // Show loading overlay
    }

    // Simulate an AJAX request
    function simulateAjaxRequest() {
        showLoading();
        setTimeout(function() {
            document.getElementById('loading-overlay').style.display = 'none'; // Hide loading overlay after 3 seconds
        }, 3000);
    }

    // Call the simulate function on page load (for demonstration)
    simulateAjaxRequest();