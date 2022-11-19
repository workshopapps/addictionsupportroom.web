import { BiTimeFive } from "react-icons/bi";
import { CiDollar } from "react-icons/ci";

const JobData = {
    Design : [
        {
            id: 1,
            Postion: 'Product Designer',
            Description: 'We’re looking for a junior-level product designer to join our team.',
            iconone: <BiTimeFive/> ,
            icontwo: <CiDollar/>,
            contract: 'Full time',
            price: '20k - 30k'

        },
        {
            id: 2,
            Postion: 'Product Designer',
            Description: 'We’re looking for a mid-level product designer to join our team.',
            iconone: <BiTimeFive/> ,
            icontwo: <CiDollar/>,
            contract: 'Full time',
            price: '40k - 60k'

        }
    ],
    SoftwareDevelopement : [
        {
            id: 1,
            Postion: 'Frontend developer',
            Description: 'We’re looking for an experienced frontend developer to join our team.',
            iconone: <BiTimeFive/> ,
            icontwo: <CiDollar/>,
            contract: 'Full time',
            price: '80k - 100k'

        }
    ]
}
export default JobData;