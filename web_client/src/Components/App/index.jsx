import React, {useState} from 'react'
import store from "../../store"
import {Provider} from 'react-redux'
import {HashRouter, Route, Switch} from "react-router-dom"
import {Container, createMuiTheme, responsiveFontSizes} from "@material-ui/core"
import {makeStyles} from "@material-ui/core/styles"
import {ThemeProvider} from "@material-ui/styles"
import HomePage from "../Pages/HomePage"
import Context from "../../context"
import NavDrawer from "../NavDrawer"
import Header from "../Header";
import BotSettingsPage from "../Pages/BotSettingsPage";
import CommandSettingsPage from "../Pages/CommandSettingsPage";
import KeyboardSettingsPage from "../Pages/KeyboardSettingsPage";
import UserSettingsPage from "../Pages/UserSettingsPage";
import StatisticsPage from "../Pages/StatisticsPage";
import Toolbar from "@material-ui/core/Toolbar";

const customTheme = createMuiTheme({
    palette: {
        primary: {
            main: '#304ffe',
            light: '#7b7cff',
            dark: '#0026ca'
        },
        secondary: {
            main: '#1de9b6',
            light: '#1de9b6',
            dark: '#00b686'
        },
        background: {
            light: '#f1f3f4'
        }
    },
    typography: {
        fontFamily: [
            'Roboto',
            'Helvetica',
            'Arial',
            'sans-serif',
        ].join(','),
    },
})

const useStyles = makeStyles((theme) => ({
    root: {

    },
    content: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        paddingTop: theme.spacing(4),
    }
}))

export default function App() {
    const classes = useStyles()

    const [isOpenDrawer, setIsOpenDrawer] = useState(false)

    const toggleDrawer = () => {
        setIsOpenDrawer(!isOpenDrawer)
    }

    return (
        <Provider store={store}>
            <ThemeProvider theme={responsiveFontSizes(customTheme)}>
                <Context.Provider value={{toggleDrawer}}>
                    <HashRouter>
                        <Header/>
                        <Toolbar/>

                        <NavDrawer open={isOpenDrawer}/>

                        <Container maxWidth="md" className={classes.content}>
                            <Switch>
                                <Route path='/' exact component={HomePage}/>
                                <Route path='/bot_settings' component={BotSettingsPage}/>
                                <Route path='/command_settings' component={CommandSettingsPage}/>
                                <Route path='/keyboard_settings' component={KeyboardSettingsPage}/>
                                <Route path='/statistics' component={StatisticsPage}/>
                                <Route path='/user_settings' component={UserSettingsPage}/>
                            </Switch>
                        </Container>
                    </HashRouter>
                </Context.Provider>
            </ThemeProvider>
        </Provider>
    )
}
