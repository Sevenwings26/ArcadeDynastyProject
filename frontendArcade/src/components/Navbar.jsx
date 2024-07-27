import React, { useState } from "react";
import { Link } from "react-router-dom";
import logo from "../images/brand-logo/logo.png";
import "../styles/Navbar.css";

const Navbar = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const handleMenuToggle = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <header>
      <nav className="flex flex-wrap items-center justify-between w-full py-4 md:py-2 px-4 md:p-5 text-lg text-gray-700 bg-white">
        <div>
          <Link to="/">
            <img src={logo} alt="Arcade Dynasty Logo" />
          </Link>
        </div>

        <button
          id="menu-button"
          className="h-6 w-6 cursor-pointer md:hidden block"
          onClick={handleMenuToggle}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>

        <div
          className={`w-full md:flex md:items-center md:w-auto ${
            menuOpen ? "" : "hidden"
          }`}
          id="menu"
        >
          <ul className="pt-4 text-base text-gray-700 md:flex md:justify-between md:pt-0">
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-purple-400"
                to="/"
              >
                Home
              </Link>
            </li>
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-purple-400"
                to="/Blog"
              >
                Blog
              </Link>
            </li>
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-purple-400"
                to="/Gallery"
              >
                Gallery
              </Link>
            </li>
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-purple-400"
                to="/about"
              >
                About
              </Link>
            </li>
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-purple-400"
                to="/Designs"
              >
                Designs
              </Link>
            </li>
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-purple-400 login-signup-link"
                to="/login"
              >
                Login
              </Link>
            </li>
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-purple-400 login-signup-link"
                to="/signup"
              >
                Sign Up
              </Link>
            </li>
          </ul>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
