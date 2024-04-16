$(document).ready(function() {
    // Get all the navbar items
    const navbarItems = $('.nav-link');

    // Add click event listener to each navbar item
    // TODO: edit this
    (navbarItems).on('click', function() {
        // Remove "active" classes from all navbar items
        navbarItems.removeClass('active');
        navbarItems.removeAttr('aria-current');

        // Add "active" classes to the clicked navbar item
        $(this).addClass('active');
        $(this).attr('aria-current', 'page');

        console.log('clicked');
    });
});
