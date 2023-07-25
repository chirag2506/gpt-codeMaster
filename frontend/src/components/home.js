import React from 'react'
import CodeImage from '../assets/code.jpg'

export default function Home() {
  const converterImgHeight = 500;
  const converterImgWidth = 650;

  console.log(converterImgHeight);
  
  return (
    <div className='sticky-footer-body'>
      <div className='py-3 px-3'>
        <span>
          <div className='d-flex align-items-center justify-content-center gap-5'>
            <img src={CodeImage} style={{ height: converterImgHeight, width: converterImgWidth }} alt="code.jpg" />
          </div>
        </span>
      </div>
    </div>
  )
}
