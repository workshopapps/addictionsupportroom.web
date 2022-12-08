import React, { useState } from "react";
import { NavLink, Link } from "react-router-dom";
import { navbarList } from "../../Data/navbar";
import Button from "../../UI/Button";
import MobileNav from "./MobileNav";
import logo from '../../assets/soberpal-logo.png'

const NavBar = () => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div>
      <div className="py-4 max-w-[1400px] w-[90%] mx-auto flex justify-between">
        <Link className="flex items-center " to="/">
          <img className="h-[4rem] w-[4rem]" src={logo} alt="soberpal logo"/>
          <p className="tablet:text-[28px]  text-[18px] text-blue font-[700]">{navbarList.logo}</p>
        </Link>
        <div>
          <ul className="hidden laptop:flex ">
            {navbarList.navList.map(({ page, link }) => (
              <NavLink className='mx-3 ' key={link}  to={link}>
                <li className="p-3 mb-2 font-[700] navbar">{page}</li>
              </NavLink>
            ))}
          </ul>
        </div>
        
        <a className="hidden laptop:block"  rel="noreferrer" href="https://appetize.io/app/3tqubo6rf6nodzau3rez6v2r5u?device=pixel4&osVersion=11.0&scale=75" target="_blank" >
          <Button className="font-[500]" text="Download App" />
        </a>

        <div
          className="flex flex-col justify-center laptop:hidden"
          onClick={() => setIsOpen(true)}
        >
          <div className="bg-blue h-[3px] w-[24px]" />
          <div className="bg-blue mt-[3px] h-[3px] w-[24px]" />
          <div className="bg-blue mt-[3px] h-[3px] w-[24px]" />
        </div>

        {isOpen && <MobileNav setIsOpen={setIsOpen} />}
      </div>
    </div>
  );
};

export default NavBar;
