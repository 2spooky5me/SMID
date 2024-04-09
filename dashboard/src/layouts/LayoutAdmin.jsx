import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { Outlet, useNavigate } from 'react-router-dom';
import { accessTokenSelector } from '../redux/reducers/UserSlicer';


const LayoutAdmin = () => {
	return (
		<>
			<div className='fondo-login-auth fondo-login-auth-no'>
				<Outlet />
			</div>
		</>
	);
};
export default LayoutAdmin;