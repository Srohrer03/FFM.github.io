import React, { useState } from 'react';
import axios from 'axios';
export default function Login({ navigate }) {
  const [u, setU] = useState('');
  const [p, setP] = useState('');
  return (
    <form onSubmit={async e => {
      e.preventDefault();
      const r = await axios.post('/api/token/', { username: u, password: p });
      localStorage.setItem('access', r.data.access);
      navigate('/dashboard');
    }}>
      <input value={u} onChange={e => setU(e.target.value)} placeholder="Username" />
      <input type="password" value={p} onChange={e => setP(e.target.value)} placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  );
}
