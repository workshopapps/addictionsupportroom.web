import React, { useState, useEffect } from "react";
import { NavLink, Link } from "react-router-dom";
import { navbarList } from "../../Data/navbar";
import Button from "../../UI/Button";
import MobileNav from "./MobileNav";
import logo from '../../assets/soberpal-logo.png'

const NavBar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [changeState, setChangeState] = useState(false)
  const [username, setUserName] = useState("");
  const [avatar, setAvatar] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("token")
    const user = localStorage.getItem("username")
    const avatar = localStorage.getItem("avatar")

    if (token) {
      setChangeState(true)
      // window.location.reload(changeState);
    } 
    
    if (user) {
      setUserName(JSON.parse(user));
    }
    if (avatar) {
      setAvatar(JSON.parse(avatar));
    }
  }, [changeState])
  return (
    <div>
      <div className="py-4 max-w-[1400px] w-[90%] mx-auto flex justify-between">
        <Link className="flex items-center " to="/">
          <img className="h-[4rem] w-[4rem]" src={logo} alt="soberpal logo" />
          <p className="tablet:text-[28px]  text-[18px] text-blue font-[700]">
            {navbarList.logo}
          </p>
        </Link>
        <div>
          <ul className="hidden laptop:flex ">
            {navbarList.navList.map(({ page, link }) => (
              <NavLink className="mx-3 " key={link} to={link}>
                <li className="p-3 mb-2 font-[700] navbar">{page}</li>
              </NavLink>
            ))}
          </ul>
        </div>
        {changeState ? (
          <div className="bg-white hidden laptop:flex items-center px-3 ">
            <img className=" w-[45px] h-[45px] border-2 border-[black] rounded-full " src={avatar} alt="fe" />
            <p className="ml-3 font-[500]">{username}</p>
          </div>
        ) : (
          <a
            className="hidden laptop:block"
            rel="noreferrer"
            href="https://appetize.io/app/q3qnqdo5ibklola6h5xlimn6rq?device=pixel4&osVersion=11.0&scale=75"
            target="_blank"
          >
            <Button className="font-[500]" text="Download App" />
          </a>
        )}

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
