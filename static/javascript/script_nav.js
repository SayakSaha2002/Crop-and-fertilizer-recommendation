// Function to handle the active class
function setActive(element) {
    // Remove the 'active' class from all <a> elements
    const links = document.querySelectorAll('ul li a');
    links.forEach(link => link.classList.remove('active'));

    // Add the 'active' class to the clicked <a> element
    element.classList.add('active');
}