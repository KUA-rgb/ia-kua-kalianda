import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

function App() {
  return (
    <Router>
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </Router>
  )
}

function Home() {
  return (
    <div className="home">
      <h1>IA KUA Kalianda</h1>
      <p>Integrated Application untuk Kantor Urusan Agama Kalianda</p>
    </div>
  )
}

export default App
