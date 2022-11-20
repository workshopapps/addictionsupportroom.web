import { BsCurrencyDollar } from "react-icons/bs";
import { BsHeart } from "react-icons/bs";
import { BsStar } from "react-icons/bs";
import { CiCalendar } from "react-icons/ci";
import { RiCalendarTodoLine } from "react-icons/ri";
import { TbBulb } from "react-icons/tb";




const ValueData = [
    {
        id: 1,
        icon: <BsCurrencyDollar className="icon" /> ,
        header: 'Competetive Salary',
        content: 'We pay you a location independent rate.'
    },
    {
        id: 2,
        icon: <BsHeart className="icon"/> ,
        header: 'End of year bonus',
        content: ' We going the extra mile.'
    },
    {
        id: 3,
        icon: <BsStar className="icon"/> ,
        header: 'Parental leave',
        content: 'We provide 3 month paid time off.'
    },
    {
        id: 4,
        icon: <CiCalendar className="icon"/> ,
        header: 'Stock options',
        content: `We don't treate "act as a owner" as a phrase.`
    },
    {
        id: 5,
        icon: <RiCalendarTodoLine className="icon"/> ,
        header: 'Health perks',
        content: 'from insurance to gym. Stay healthy!'
    },
    {
        id: 6,
        icon: <TbBulb className="icon"/> ,
        header: 'Flexible time off',
        content: 'We recommend at least 25 days.'
    }
]

export default ValueData;