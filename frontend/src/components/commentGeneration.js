import React from 'react';

export default function CommentGeneration() {

  return (
    <div className='sticky-footer-body'>
      <div className='py-3 px-3'>
        <div className='d-flex align-items-center justify-content-center gap-5'>
          CommentGeneration
        </div>
        <div className='d-flex align-items-center justify-content-center gap-5'>
          <div>
            <textarea id="userQuestion" rows="8" cols="55" placeholder="write or paste your code here..."
              className="codeArea"></textarea>
            <button id="botAction" className="btnProcess">Validate</button>
          </div>
          <textarea id="botResponse" rows="8" cols="55" placeholder="" className="codeArea"></textarea>
        </div>
      </div>
    </div>
  )
}
