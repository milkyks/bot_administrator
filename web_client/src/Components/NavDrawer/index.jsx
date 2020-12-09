import React, {useContext} from 'react'
import {makeStyles} from '@material-ui/core/styles'
import Drawer from '@material-ui/core/Drawer'
import List from '@material-ui/core/List'
import Context from "../../context"
import {useHistory} from "react-router-dom"
import ListItem from "@material-ui/core/ListItem"
import ListItemText from "@material-ui/core/ListItemText"
import Typography from "@material-ui/core/Typography";
import {Toolbar} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    root: {
        height: '100%',
    },
    list: {
        width: 250,
    }
}))

const pages = [
    {
        title: 'Главная',
        path: ''
    },
    {
        title: 'Настройки бота',
        path: 'bot_settings'
    },
    {
        title: 'Настройки команд',
        path: 'command_settings'
    },
    {
        title: 'Настройки клавиатуры',
        path: 'keyboard_settings'
    },
    {
        title: 'Статистика',
        path: 'statistics'
    }
]

export default function NavDrawer({open}) {
    const classes = useStyles()
    const history = useHistory()

    const {toggleDrawer} = useContext(Context)

    const goPage = (pagePath) => {
        history.push(`/${pagePath}`)
        toggleDrawer()
    }

    return (
        <Drawer
            anchor='left'
            open={open}
            onClose={() => toggleDrawer()}
        >
            <Toolbar>
                <Typography variant="h6">
                    Dorm bot
                </Typography>
            </Toolbar>
            <List className={classes.list}>
                {pages.map(page =>
                    <ListItem
                        button
                        key={page.path}
                        onClick={() => goPage(page.path)}>
                        <ListItemText primary={page.title}/>
                    </ListItem>
                )}
            </List>
        </Drawer>
    )
}
