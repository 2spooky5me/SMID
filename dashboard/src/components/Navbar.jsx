//? COMPONENTS
import IconButton from '@mui/material/IconButton';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
//? ICONS
import { IoMenuSharp } from "react-icons/io5";
import { MdOutlineAdminPanelSettings } from 'react-icons/md';
import { RiLogoutBoxLine } from 'react-icons/ri';
//? HOOKS
import { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import UseAxios from '/src/hooks/UseAxios';
//? REDUX
import { usernameSelector, unSetUser } from '/src/redux/reducers/UserSlicer'
const Navbar = () => {
	//* HOOKS
	const navigate = useNavigate();
	const request = UseAxios()
	const username = useSelector(usernameSelector);
	const dispatch = useDispatch();
	//* MENU
	const [anchorEl, setAnchorEl] = useState(null);
	const open = Boolean(anchorEl);
	const handleClick = (event) => {
		setAnchorEl(event.currentTarget);
	};
	const handleClose = () => {
		setAnchorEl(null);
	};
	const logoutEvent = () => {
		request('POST', 'logout/', { username }).finally(() => {
			dispatch(unSetUser());
			navigate('auth/');
		})
	};
	return (
		<div className='print-hidden grid grid-cols-2 h-[50px] p-1 pr-3 w-full border-b theme-border bg-gradient-to-b from-neutral-100 to-neutral-300'>
			< nav className='flex items-center justify-start p-2' >

			</nav >
			<nav className='flex items-center justify-end gap-4'>

				<IconButton
					aria-label="open"
					id="basic-button"
					aria-controls={open ? 'basic-menu' : undefined}
					aria-expanded={open ? 'true' : undefined}
					onClick={handleClick}>
					<IoMenuSharp className='' />
				</IconButton>
				<Menu
					id="basic-menu"
					anchorEl={anchorEl}
					open={open}
					onClose={handleClose}
				>
					<MenuItem
						onClick={() => window.location.href = import.meta.env.VITE_APP_API_URL + 'admin/'}
						className='navMenuItem'
					>
						<MdOutlineAdminPanelSettings className='m-1 text-primary-500' />
						Administrador
					</MenuItem>
					<MenuItem
						onClick={logoutEvent}
						className='navMenuItem'
					>
						<RiLogoutBoxLine className='m-1 text-primary-500' />
						Cerrar sesión
					</MenuItem>
				</Menu>
			</nav>
		</div >
	);
};

export default Navbar;
