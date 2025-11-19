import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const hostname = window.location.hostname;
  const endpoint = hostname.includes('-8000.app.github.dev')
    ? `https://${hostname}/api/teams/`
    : 'http://localhost:8000/api/teams/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Teams endpoint:', endpoint);
        console.log('Fetched teams:', data);
        setTeams(data.results || data);
      });
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-header bg-primary text-white">
        <h2 className="h4">Teams</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Name</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team, idx) => (
              <tr key={idx}>
                <td>{team.name}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Teams;
