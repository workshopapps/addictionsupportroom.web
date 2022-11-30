import { Link } from 'react-router-dom'
import './newscard.scss'

const NewsCard = () => {
  return (
    <div className='newscard' >
        <div>
        <p className='news__id' >Soberpal#167</p>
           <p>15 Nov, 2022</p> 
        </div>
        <h4>How to use stay sober in the fastest way!</h4>
        <p>With Soberpal App, staying sober is just a very easy thing to do . . .</p>
        <Link  className='li'>More</Link>
    </div>
  )
}

export default NewsCard