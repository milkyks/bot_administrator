import React from "react"
import {makeStyles} from "@material-ui/core/styles"
import {Typography} from "@material-ui/core"

import vk_logo from './icons/vk.svg'
import tg_logo from './icons/telegram.svg'
import gmail_logo from './icons/gmail.svg'

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column'
    },
    row: {
        display: "flex",
        alignItems: "center",
        marginBottom: theme.spacing(1)
    },
    title: {
        marginBottom: theme.spacing(1)
    },
    value: {
        marginLeft: theme.spacing(1)
    }
}))

export default function HomePage() {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <Typography variant='h6' className={classes.row}>
                Для чего это веб-приложение?
            </Typography>
            <Typography>
                С помощью данного веб-приложения можно изменить настройки бота, добавить и/или удалить команды, изменить клавиатуру бота, а также посмотреть частоту использования команд за любой промежуток времени. 
            </Typography>
            <br/>
            <Typography variant='h6' className={classes.row}>
                Как пользоваться?
            </Typography>
            <Typography>
                 На вкладке "Настройки бота" можно изменить токен и id группы, ссылки на ответственных за спортзал и учебную комнату, а также ссылку на хранилище чеков. На вкладке "Настройки команд" вы можете добавлять новые команды, редактировать старые либо удалять их. На вкладке "Настройки клавиатуры" можно изменять клавиатуру бота: добавлять новые команды, удалять их или менять местами. На вкладке "Статистика" доступна возможность посмотреть частоту использования команд бота за разный промежуток времени. <br /><br />
                При нажатии на иконку пользователя открывается подменю. На странице с настройками пользователя можно редактировать свои данные либо же добавить в систему нового пользователя. Также при помощи подменю можно выйти из системы.
            </Typography>
            <br/>
            <Typography variant='h6' className={classes.title}>
                Наши контактные данные
            </Typography>
            <div>
                <div className={classes.row}>
                    <img src={vk_logo} width={30} />
                    <Typography className={classes.value}>
                        <a href="https://vk.com/re_giorgio">https://vk.com/re_giorgio</a>
                    </Typography>
                </div>
                <div className={classes.row}>
                    <img src={tg_logo} width={30} />
                    <Typography className={classes.value}>
                        @dumaevrinat, @kseniyababintseva
                    </Typography>
                </div>
                <div className={classes.row}>
                    <img src={gmail_logo} width={30} />
                    <Typography className={classes.value}>
                        alina.lobanova@gmail.com
                    </Typography>
                </div>
            </div>
        </div>
    )
}
