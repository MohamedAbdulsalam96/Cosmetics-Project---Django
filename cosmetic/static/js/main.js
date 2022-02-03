let navbar = document.querySelector('.navbar')
document.querySelector('#menu-btn').onclick = () => {
    navbar.classList.toggle('active')
}

document.querySelector('#close-navbar').onclick = () => {
    navbar.classList.remove('active')
}

let searchForm = document.querySelector('.search-form')
document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active')
}

window.onscroll = () => {
    navbar.classList.remove('active')
    searchForm.classList.remove('active')
}

let slides = document.querySelectorAll('.home .slide');
let index = 0;

function next() {
    slides[index].classList.remove('active')
    index = (index + 1) % slides.length
    slides[index].classList.add('active')
}
function prev() {
    slides[index].classList.remove('active')
    index = (index - 1 + slides.length) % slides.length
    slides[index].classList.add('active')
}
var swiper = new Swiper(".products-slider", {
    loop: true,
    grapCursor: true,
    spaceBetween: 20,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
          slidesPerView: 1,
        },
        550: {
          slidesPerView: 2,
        },
        850: {
          slidesPerView: 3,
        },
        1200: {
          slidesPerView: 4,
        },
      },
  });
var swiper = new Swiper(".arrivals-slider", {
    loop: true,
    grapCursor: true,
    spaceBetween: 20,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
          slidesPerView: 1,
        },
        550: {
          slidesPerView: 2,
        },
        850: {
          slidesPerView: 3,
        },
        1200: {
          slidesPerView: 4,
        },
      },
  });
var swiper = new Swiper(".blogs-slider", {
    loop: true,
    grapCursor: true,
    spaceBetween: 20,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
          slidesPerView: 1,
        },
        550: {
          slidesPerView: 2,
        },
        850: {
          slidesPerView: 3,
        },
        1200: {
          slidesPerView: 4,
        },
      },
  });
lightGallery(document.querySelector('.gallery .lightBox'))

var swiper = new Swiper(".review-slider", {
    spaceBetween: 20,
    loop: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      991: {
        slidesPerView: 3,
      },
    },
  });







