import React from "react";
import { Link } from "react-router-dom";
import Logout from "./Logout";

const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white font-bold">Fashion Model</div>
        <div className="space-x-4">
          <Link to="/" className="text-white">
            Home
          </Link>
          <Link to="/about" className="text-white">
            About
          </Link>
          <Link to="/login" className="text-white">
            Login
          </Link>
          <Logout />
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
