const likeImage = document.querySelectorAll(".like_image");
const emptyLike =
  "https://res.cloudinary.com/intellectfox/image/upload/v1629752957/fe/foxgram/posts/like_xw2apm.svg";
const fullLike =
  "https://res.cloudinary.com/intellectfox/image/upload/v1629752958/fe/foxgram/posts/like-filled_zurlii.svg";

likeImage.forEach((like_element) => {
  like_element.addEventListener("click", (event) => {
    const likeCountEl = event.target.parentElement.querySelector(".like_count");
    const likeCount = +likeCountEl.textContent;
    if (event.target.src === emptyLike) {
      event.target.src = fullLike;
      likeCountEl.textContent = likeCount + 1;
    } else {
      event.target.src = emptyLike;
      likeCountEl.textContent = likeCount - 1;
    }
  });
});
