import React from 'react'

export default function CodeGeneration() {

  return (
    <div className='sticky-footer-body'>
      <div className='py-3 px-3'>
        <div className='d-flex align-items-center justify-content-center gap-5'>
          CodeGeneration
        </div>
        <div className='d-flex align-items-center justify-content-center gap-5'>
          <div>
            <input type="text" id="userQuestion" rows="8" cols="55" placeholder="query"
              className="codeArea" />
            <button id="botAction" className="btnProcess">Generate</button>
          </div>
          <textarea id="botResponse" rows="8" cols="55" placeholder="" className="codeArea"></textarea>
        </div>
      </div>
    </div>
  )
}
