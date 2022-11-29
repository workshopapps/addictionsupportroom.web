import { BiUser } from "react-icons/bi";
import { BsHeart } from "react-icons/bs";
import { AiOutlineLineChart } from "react-icons/ai";
import { CiFaceSmile } from "react-icons/ci";
import { RiFlag2Line } from "react-icons/ri";
import { TiFlashOutline } from "react-icons/ti";




const ValueData = [
    {
        id: 1,
        icon: <BiUser className="icon" /> ,
        header: 'Care about our team',
        content: 'Understand what matters to our employees. Give them what they need to do their best work.'
    },
    {
        id: 2,
        icon: <BsHeart className="icon"/> ,
        header: 'Be excellent to each other',
        content: ' We rely on our peers to improve. Be open,honest and kind.'
    },
    {
        id: 3,
        icon: <AiOutlineLineChart className="icon"/> ,
        header: 'Pride in what we do',
        content: 'Value quality and integrity in everything we do. At all times. No exceptions.'
    },
    {
        id: 4,
        icon: <CiFaceSmile className="icon"/> ,
        header: 'Care about our customer',
        content: 'Understand customers stated and unstated needs. '
    },
    {
        id: 5,
        icon: <RiFlag2Line className="icon"/> ,
        header: 'Do the impossible',
        content: 'Be energized by difficult problems. Revel in unknowns. Ask "Why?", but always question, "Why not?"'
    },
    {
        id: 6,
        icon: <TiFlashOutline className="icon"/> ,
        header: 'Sweat the small stuff',
        content: 'We believe the best products come from the best, attention to detail. Sweat the small stuff.'
    }
]

export default ValueData;
