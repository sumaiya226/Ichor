let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.header .nav');




menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () => {
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');

    if (window.scrollY > 0) {
        document.querySelector('.header').classList.add('active');
    } else {
        document.querySelector('.header').classList.remove('active');
    }
}

let searchform = document.querySelector(".search-form");

document.querySelector("#search-btn").onclick = () => {
    searchform.classList.toggle("active");
}








document.addEventListener("DOMContentLoaded", function () {
    const userBtn = document.getElementById("user-btn");
    const subMenu = document.getElementById("subMenu");

    userBtn.addEventListener("click", function () {
        // Toggle the visibility of the sub-menu
        subMenu.style.display = subMenu.style.display === "none" ? "block" : "none";
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const userBtn = document.getElementById("user-btn");
    const subMenu = document.getElementById("subMenu");
    const loginOption = document.getElementById("login-option");

    // Function to open the login page
    function openLoginPage() {
        // Replace "login.html" with the actual URL of your login page
        window.location.href = "/templates/login.html";
    }

    loginOption.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the default link behavior
        openLoginPage(); // Call the function to open the login page
    });
});


// Function to open the profile page
function openProfilePage() {
    // Replace 'profile.html' with the actual URL of your profile page
    window.location.href = '/templates/profile.html';
  }

// Function to open the request page
function openRequestPage() {
    // Replace 'request.html' with the actual URL of your request page
    window.location.href = '/templates/request.html';
}

  // Function to open the donate page
function openDonatePage() {
    // Replace 'donate.html' with the actual URL of your donate page
    window.location.href = '/templates/donate.html';
  }

  // Function to open the blog page
  function openBlogPage() {
    // Replace 'blog-page.html' with the actual URL of your blog's main page
    window.location.href = "https://donateblood2.blogspot.com/";
}

function openFindPage() {
    // Replace 'donate.html' with the actual URL of your donate page
    window.location.href = '/templates/find.html';
  }

  