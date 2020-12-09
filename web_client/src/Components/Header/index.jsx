import React, {useContext} from 'react'
import {makeStyles} from '@material-ui/core/styles'
import {useHistory} from 'react-router-dom'
import Context from '../../context'
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Typography from '@material-ui/core/Typography';
import AppBar from '@material-ui/core/AppBar';
import {AccountCircle} from '@material-ui/icons';
import ClickAwayListener from '@material-ui/core/ClickAwayListener';
import Grow from '@material-ui/core/Grow';
import Paper from '@material-ui/core/Paper';
import Popper from '@material-ui/core/Popper';
import MenuItem from '@material-ui/core/MenuItem';
import MenuList from '@material-ui/core/MenuList';

const useStyles = makeStyles((theme) => ({
    root: {

    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    title: {
    },
    menu: {
        marginLeft: 'auto'
    }
}))

export default function Header() {
    const classes = useStyles()
    const history = useHistory()

    const {toggleDrawer} = useContext(Context)

    const [open, setOpen] = React.useState(false);
    const anchorRef = React.useRef(null);

    const handleToggle = () => {
        setOpen((prevOpen) => !prevOpen);
    };

    const handleClose = (event) => {
        if (anchorRef.current && anchorRef.current.contains(event.target)) {
            return;
        }

        setOpen(false);
    };

    const prevOpen = React.useRef(open);
    React.useEffect(() => {
        if (prevOpen.current === true && open === false) {
            anchorRef.current.focus();
        }

        prevOpen.current = open;
    }, [open]);

    const goPage = (pagePath) => {
        history.push(`/${pagePath}`)
        handleToggle()
    }

    return (
        <AppBar color='inherit' position="fixed" elevation={0}>
            <Toolbar>
                <IconButton edge="start" className={classes.menuButton} color="inherit" onClick={() => toggleDrawer()}>
                    <MenuIcon />
                </IconButton>
                <Typography variant="h6" className={classes.title}>
                    Dorm bot
                </Typography>

                <div className={classes.menu}>
                        <IconButton
                            color="inherit"
                            ref={anchorRef}
                            aria-controls={open ? 'menu-list-grow' : undefined}
                            aria-haspopup="true"
                            onClick={handleToggle}
                        >
                            <AccountCircle />
                        </IconButton>
                        <Popper open={open} anchorEl={anchorRef.current} role={undefined} transition disablePortal>
                          {({ TransitionProps, placement }) => (
                            <Grow
                              {...TransitionProps}
                              style={{ transformOrigin: placement === 'bottom' ? 'center top' : 'center bottom' }}
                            >
                              <Paper>
                                <ClickAwayListener onClickAway={handleClose}>
                                  <MenuList autoFocusItem={open} id="menu-list-grow">
                                    <MenuItem onClick={() => goPage('user_settings')}>Настройки пользователя</MenuItem>
                                    <MenuItem onClick={handleClose}>Выйти из системы</MenuItem>
                                  </MenuList>
                                </ClickAwayListener>
                              </Paper>
                            </Grow>
                          )}
                        </Popper>
                </div>
            </Toolbar>
        </AppBar>
    )
}
