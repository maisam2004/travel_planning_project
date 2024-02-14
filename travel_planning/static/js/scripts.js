
    $(document).ready(function () {

        var originalText = $('#addDestinationText').text();

        // Change the text on hover
        $('.btn-primary').hover(
            function () {
                $('#addDestinationText').text('Login first');
            },
            function () {
                // Restore the original text when not hovering
                $('#addDestinationText').text(originalText);
            }
        );

        
   
    $('.like-button').click(function() {
        var icon = $(this);
        if (icon.hasClass('liked')) {
            icon.removeClass('liked').addClass('notliked'); // change class for unlike
        } else {
            icon.removeClass('notliked').addClass('liked'); // change class for like
        }
    });

        var originalBackgroundImage = $('#hero-section').css('background-image');
        var originalTitleText = $('#hero-title').text();
        var originalLeadText = $('#hero-text').text();

        var scrollTriggerPosition = 1000;
        var scrollTriggerPosition2 = 5600;
        $(window).scroll(function() {
            // Get the height of the featured destinations section
            //var featuredDestinationsHeight = $('.container.mt-5').offset().top;

            // Get the height of the hero section
            //var heroSectionHeight = $('.hero-container').height();

            // Calculate the scroll position
           // var scrollPosition = $(window).scrollTop();
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

    });