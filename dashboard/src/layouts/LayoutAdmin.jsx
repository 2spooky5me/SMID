// import { useEffect } from 'react';
// import { useSelector } from 'react-redux';
import { Outlet, useNavigate } from 'react-router-dom';
// import { accessTokenSelector } from '../redux/reducers/UserSlicer';
// import Sidebar from '../components/Sidebar';
// import Navbar from '/src/components/Navbar/Navbar';
//import Navbar from '../components'

const LayoutAdmin = () => {
	// const navigate = useNavigate();
	// const token = useSelector(accessTokenSelector);
	// useEffect(() => {
	// 	if (token === '') {
	// 		navigate('auth/');
	// 	};
	// }
	// 	, []);
	return (
		<>
			<div className='fondo-login-auth fondo-login-auth-no'>
				<Outlet />
			</div>
		</>
	);
};
export default LayoutAdmin;