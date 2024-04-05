import { BrowserRouter, Route, Routes } from 'react-router-dom';
//* Layout
import LayoutAuth from '/src/layouts/LayoutAuth';
import LayoutAdmin from '/src/layouts/LayoutAdmin';
//! Pages Auth
import Login from '/src/pages/auth/Login';
//! Pages Admin
import Home from '/src/pages/admin/Home';


function App() {

  return (

      <BrowserRouter>
        <Routes>
          <Route path='/auth' element={<LayoutAuth />}>
            <Route index element={<Login />} />
          </Route>
          <Route path='/' element={<LayoutAdmin />}>
            <Route index element={<Home />} />
          </Route>
        </Routes>
      </BrowserRouter>
  );
}
export default App;