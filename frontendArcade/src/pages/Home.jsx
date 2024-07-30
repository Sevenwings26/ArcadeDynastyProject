import React from "react";
import Carousel from "../components/Carousel";
import "../styles/Navbar.css";

const Home = () => {
  return (
    <div className="">
      {/* <Carousel /> */}
      <div>
        <div className="flex flex-col items-center text-center py-8">
          <div>
            <h2 className="text-3xl font-bold mb-2">Arcade Fashion Week</h2>
            <p className="max-w-md">Recent updates on models, runway trends, and casual fashion, featuring both seasoned supermodels and emerging talents.</p>
          </div>
        </div>
        <div className="arcade-display">
          <div className="arcade-display-absolute">
            <a href="#" className="arcade-views">
              <div className="arcade-display-absolute-bg">View More</div>
            </a>
            <div className="arcade-display-absolute-border"></div>
          </div>
        </div>
      </div>
</div>
  );
};

export default Home;
