$(document).ready(function () {

        let originalText = $('#addDestinationText').text();

        // Change the text on hover
        // explore page 
        $('.btn-primary').hover(
            function () {
                $('#addDestinationText').text('Login first');
            },
            function () {
                // Restore the original text when not hovering
                $('#addDestinationText').text(originalText);
            }
        );

        
   
 

       /*  var originalBackgroundImage = $('#hero-section').css('background-image');
        var originalTitleText = $('#hero-title').text();
        var originalLeadText = $('#hero-text').text();

        var scrollTriggerPosition = 1000;
        var scrollTriggerPosition2 = 5600;
        $(window).scroll(function() {
           
           var scrollPosition = $(window).scrollTop();

            // Check if the scroll position is below the featured destinations section
            if (scrollPosition >= scrollTriggerPosition2) {
                // Change the background image and text for scrollTriggerPosition2
                $('#hero-section').css('background-image', 'url("/static/images/background/hero_img.png")');
                $('#hero-title').text('Please fill the form ');
                $('#hero-text').text('we try to find what you realy after');
            } else if (scrollPosition >= scrollTriggerPosition) {
                // Change the background image and text for scrollTriggerPosition
                $('#hero-section').css('background-image', 'url("/static/images/background/night_bg.jpg")');
                $('#hero-title').text('Inspire yourself');
                $('#hero-text').text('Embark on a Journey Of Lifetime');
            } else {
                // Revert back to the original background image and text
                $('#hero-section').css('background-image', originalBackgroundImage);
                $('#hero-title').text(originalTitleText);
                $('#hero-text').text(originalLeadText);
            }
        });
 */
        // home page 

        // for hotel stars 
        $(".special").each(function() { 
            // Check if the list item is empty
            if ($(this).children().length === 0) {
                // Append the word "Special" to the list item
                $(this).html("Special Place <i class=\"fa-solid fa-star text-wrning \"></i>");
            }
        });

        
        $('.show-more-btn').on('click', function() {
            $('.travel-package.d-none').slice(0, 4).removeClass('d-none'); // Show more deals
            if ($('.travel-package.d-none').length === 0) {
                $('.show-more-btn').hide();
                
            }
        }); 
  
  
  
        // for hotel stars show cards slowly 
        $('.card').click(function() {
      let packageId = $(this).data('package-id');
      $('#destinationModal' + packageId).modal('show'); // Show the corresponding modal
    });
  
  
  
  const $cards = $('.travel-package');
  
    // Set up the fading animation
    $cards.each(function() {
      $(this).css('opacity', '0');
    });
  
    // Function to check if an element is in view
    function isElementInViewport(el) {
      const rect = el.getBoundingClientRect();
      return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    }
  
    // Function to fade in the cards when they come into view
    function fadeInCards() {
      $cards.each(function() {
        if (isElementInViewport(this)) {
          $(this).animate({ opacity: 1 }, 1000); // Adjust the duration as needed
        }
      });
    }
  
    // Call the fadeInCards function when the page is scrolled
    $(window).scroll(function() {
      fadeInCards();
    });
  
    // Call the fadeInCards function initially
    fadeInCards();
  


    });