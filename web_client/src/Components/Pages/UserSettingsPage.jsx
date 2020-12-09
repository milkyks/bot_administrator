import React, {useState} from "react"
import {makeStyles} from "@material-ui/core/styles"
import {Typography} from "@material-ui/core"
import {useDispatch, useSelector} from "react-redux"
import {fetchCommands, selectAllCommands} from "../../slices/commandsSlice"
import CircularProgress from "@material-ui/core/CircularProgress"
import Card from "@material-ui/core/Card"
import CardActions from "@material-ui/core/CardActions"
import Button from "@material-ui/core/Button"
import Radio from '@material-ui/core/Radio'
import RadioGroup from '@material-ui/core/RadioGroup'
import TextField from '@material-ui/core/TextField'
import FormControlLabel from '@material-ui/core/FormControlLabel'

const useStyles = makeStyles((theme) => ({
    root: {
        maxWidth: '100%',
        display: "flex",
        flexDirection: 'column',
    },
    info: {
        marginRight: theme.spacing(20)
    },
    card: {
        padding: theme.spacing(2),
        marginTop: theme.spacing(1),
        marginBottom: theme.spacing(1)
    },
    row: {
        display: "flex",
        alignItems: "center",
        marginBottom: theme.spacing(1)
    },
    key: {
        color: 'gray'
    },
    value: {
        marginLeft: theme.spacing(2)
    },
    actions: {
        marginTop: theme.spacing(2),
        justifyContent: 'center'
    },
    button: {
        color: 'white',
        backgroundColor: '#4599D6',
        borderRadius: theme.spacing(5),
        '&:hover': {
            backgroundColor: '#4599D6'
        }
    }
}))

export default function CommandSettingsPage() {

    const classes = useStyles()
    const [pressedEditButton, setPressedEditButton] = useState(false)

    const Label = (props) => (
        <Typography className={classes.value}>
            {props.text}
        </Typography>
    )

    const LoginTextField = (props) => (
        <TextField className={classes.value} variant="outlined" size="small" defaultValue={props.text} />
    )

    const PasswordTextField = (props) => (
        <TextField className={classes.value} type="password" variant="outlined" size="small" defaultValue={props.text} />
    )

    return (
        <div className={classes.root}>
            <Typography className={classes.info}>
                Редактирование данных
            </Typography>
            <Card variant="outlined" className={classes.card}>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Логин
                    </Typography>
                    { pressedEditButton ? <LoginTextField text="admin" /> : <Label text="admin" /> }
                </div>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Пароль
                    </Typography>
                    { pressedEditButton ? <PasswordTextField text="0123456789" /> : <Label text="●●●●●●●●●●" /> }
                </div>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Статус
                    </Typography>
                    <Typography  className={classes.value}>
                        Администратор
                    </Typography>
                </div>

                <CardActions className={classes.actions}>
                    <Button className={classes.button} onClick={() => setPressedEditButton(!pressedEditButton)}>
                        { pressedEditButton ? "Сохранить" : "Редактировать" }
                    </Button>
                </CardActions>
            </Card>
            <br />
            <Typography className={classes.info}>
                Добавление нового пользователя
            </Typography>
            <Card variant="outlined" className={classes.card}>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Логин
                    </Typography>
                    <TextField className={classes.value} variant="outlined" size="small" />
                </div>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Пароль
                    </Typography>
                    <TextField className={classes.value} type="password" variant="outlined" size="small" />
                </div>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Статус
                    </Typography>
                    <RadioGroup className={classes.value} row defaultValue="admin">
                        <FormControlLabel value="admin" control={<Radio color="primary" />} label="Администратор" />
                        <FormControlLabel value="editor" control={<Radio color="primary" />} label="Редактор" />
                    </RadioGroup>
                </div>

                <CardActions className={classes.actions}>
                    <Button className={classes.button}>
                        Сохранить
                    </Button>
                </CardActions>
            </Card>
        </div>
    )
}
