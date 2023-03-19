import React, { useState } from 'react';
import './LeadComponent.css';

const Leads = ({ showLeads, scrapedResults }) => {
  const [expanded, setExpanded] = useState(false);
  const [selectedResult, setSelectedResult] = useState({});

  const handleClick = (result) => {
    setSelectedResult(result);
    setExpanded(!expanded);
  };

  return (
    <>
      {showLeads && (
        <div className="results-container">
          <h1 className="results-header">Leads</h1>
          <div className="results-list">
            {scrapedResults.map((result, index) => (
              <div key={index} className="result-box" onClick={() => handleClick(result)}>
                <p className="result-username">{result["username"]}</p>
              </div>
            ))}
          </div>
          {expanded && (
            <div className="result-details-container">
              <div className="result-details-box">
                <p className="result-detail-label">Followers:</p>
                <p className="result-detail">{selectedResult["followers"]}</p>
                <p className="result-detail-label">Page:</p>
                <p className="result-detail">{selectedResult["url"]}</p>
                <p className="result-detail-label">Link:</p>
                <p className="result-detail">{selectedResult["link"]}</p>
              </div>
            </div>
          )}
        </div>
      )}
    </>
  );
};

export default Leads;
