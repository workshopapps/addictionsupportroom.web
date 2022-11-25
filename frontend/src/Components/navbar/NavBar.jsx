import React, { useState } from "react";
import { NavLink, Link } from "react-router-dom";
import { navbarList } from "../../Data/navbar";
import Button from "../../UI/Button";
import MobileNav from "./MobileNav";

const NavBar = () => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div>
      <div className="py-4 max-w-[1400px] w-[90%] mx-auto flex justify-between">
        <Link to="/">
          <p className="tablet:text-[32px] text-[24px] text-blue font-[700]">{navbarList.logo}</p>
        </Link>
        <div>
          <ul className="hidden laptop:flex">
            {navbarList.navList.map(({ page, link }) => (
              <NavLink className='mx-3 ' key={link}  to={link}>
                <li className="p-4 pb-2 font-[700] ">{page}</li>
              </NavLink>
            ))}
          </ul>
        </div>
        <Link className="hidden laptop:block" to={navbarList.appLink}>
          <Button text={navbarList.app} />
        </Link>

        <div
          className="flex flex-col justify-center laptop:hidden"
          onClick={() => setIsOpen(true)}
        >
          <div className="bg-blue h-[3px] w-[24px]" />
          <div className="bg-blue mt-[3px] h-[3px] w-[24px]" />
        </div>

        {isOpen && <MobileNav setIsOpen={setIsOpen} />}
      </div>
    </div>
  );
};

export default NavBar;
