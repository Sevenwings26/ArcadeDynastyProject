import React, { useState } from "react";
import { Link } from "react-router-dom";
import logo from "../images/brand-logo/logo.png";
import "../styles/Navbar.css";

const Navbar = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  const handleMenuToggle = () => {
    setMenuOpen(!menuOpen);
  };

  const handleDropdownToggle = () => {
    setDropdownOpen(!dropdownOpen);
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
              <Link className="md:p-3 py-2 m-2 block hover:text-gray-400" to="/">
                Home
              </Link>
            </li>
            <li>
              <Link className="md:p-3 py-2 m-2 block hover:text-gray-400" to="/Blog">
                Blog
              </Link>
            </li>
            <li className="relative">
              <button
                className="md:p-3 py-2 m-2 block hover:text-gray-400 focus:outline-none"
                onClick={handleDropdownToggle}
              >
                Gallery <span>🔽</span>
              </button>
              {dropdownOpen && (
                <ul className="absolute bg-white shadow-md rounded-lg mt-2">
                  <li>
                    <Link
                      className="block px-4 py-2 hover:bg-gray-100"
                      to="/Gallery/Event1"
                    >
                      Arcade Fashion Week
                    </Link>
                  </li>
                  <li>
                    <Link
                      className="block px-4 py-2 hover:bg-gray-100"
                      to="/Gallery/Event2"
                    >
                      Event 2
                    </Link>
                  </li>
                  <li>
                    <Link
                      className="block px-4 py-2 hover:bg-gray-100"
                      to="/Gallery/Event3"
                    >
                      Event 3
                    </Link>
                  </li>
                  <li>
                    <Link
                      className="block px-4 py-2 hover:bg-gray-100"
                      to="/Gallery/Event4"
                    >
                      Event 4
                    </Link>
                  </li>
                </ul>
              )}
            </li>
            <li>
              <Link className="md:p-3 py-2 m-2 block hover:text-gray-400" to="/about">
                About
              </Link>
            </li>
            <li>
              <Link className="md:p-3 py-2 m-2 block hover:text-gray-400" to="/Designs">
                Designs
              </Link>
            </li>
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-gray-400"
                to="/login"
              >
                Login
              </Link>
            </li>
            <li>
              <Link
                className="md:p-3 py-2 m-2 block hover:text-gray-400"
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

