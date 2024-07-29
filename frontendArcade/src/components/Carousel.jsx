// src/components/Carousel.jsx
import React, { useState, useEffect } from "react";
import image1 from "../images/carousel/image1.jpg";
import image2 from "../images/carousel/image2.jpg";
import image3 from "../images/carousel/image3.jpg";
import image4 from "../images/carousel/image4.jpg";
import image5 from "../images/carousel/image5.jpg";
import image7 from "../images/carousel/image7.jpg";
import image8 from "../images/carousel/image8.jpg";
import image6 from "../images/carousel/image6.jpg";

const images = [image1, image2, image3, image4, image5, image6, image7, image8];

const Carousel = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => {
      setWindowWidth(window.innerWidth);
    };

    window.addEventListener("resize", handleResize);

    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 3000); // Change image every 3 seconds

    return () => {
      window.removeEventListener("resize", handleResize);
      clearInterval(interval);
    };
  }, []);

  const visibleImages = windowWidth < 640 ? 1 : 3; // 1 image for screens smaller than 640px, otherwise 3

  const currentImages = [];
  for (let i = 0; i < visibleImages; i++) {
    currentImages.push(images[(currentIndex + i) % images.length]);
  }

  return (
    <div className="overflow-hidden w-full">
      <div
        className="flex transition-transform duration-1000"
        style={{
          transform: `translateX(-${
            (currentIndex % images.length) * (100 / visibleImages)
          }%)`,
        }}
      >
        {currentImages.map((image, index) => (
          <div key={index} className="flex-shrink-0 w-full sm:w-1/3 p-2">
            <img
              src={image}
              alt={`Slide ${index}`}
              className="w-full h-full object-cover"
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Carousel;
