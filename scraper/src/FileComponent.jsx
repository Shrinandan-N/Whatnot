import React, { useRef } from 'react';

const FileInput = ({ onChange, ...rest }) => {
  const inputRef = useRef();

  const handleButtonClick = () => {
    inputRef.current.click();
  };

  const handleInputChange = (e) => {
    if (onChange) {
      onChange(e.target.files[0]);
    }
  };

  return (
    <div className="file-input">
      <input
        type="file"
        ref={inputRef}
        onChange={handleInputChange}
        style={{ display: 'none' }}
      />
      <button onClick={handleButtonClick} {...rest}>
        <span>Choose File</span>
      </button>
    </div>
  );
};

export default FileInput;
