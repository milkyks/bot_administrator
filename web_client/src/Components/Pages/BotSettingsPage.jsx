import React, {useState} from "react"
import {makeStyles} from "@material-ui/core/styles"
import {Typography} from "@material-ui/core"
import Card from "@material-ui/core/Card"
import CardActions from "@material-ui/core/CardActions"
import Button from "@material-ui/core/Button"
import TextField from '@material-ui/core/TextField'

const useStyles = makeStyles((theme) => ({
    root: {
        maxWidth: '100%',
        display: "flex",
        flexDirection: 'column',
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

export default function BotSettingsPage() {

    const classes = useStyles()
    const [pressedEditButton, setPressedEditButton] = useState(false)

    const Label = (props) => (
        <Typography className={classes.value}>{props.text}</Typography>
    )

    const Field = (props) => (
        <TextField className={classes.value} variant="outlined" size="small" defaultValue={props.text} />
    )

    var token = 'ob566rfrgtgtefiiejr444dkfmkgmkkdfffdlfkgorpdkglqkhoprofjd5g9l3so'
    var group_id = 123456789
    var sport_resp_link = 'https://vk.com/resp1'
    var train_resp_link = 'https://vk.com/resp2'
    var receipts_link = 'https://drive.google.com/drive/folders/1GqGyHz3...'

    return (
        <div className={classes.root}>
            <Typography className={classes.info}>
                Изменение настроек бота
            </Typography>
            <Card variant="outlined" className={classes.card}>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Токен
                    </Typography>
                    { pressedEditButton ? <Field text={token} /> : <Label text={token} /> }
                </div>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        ID группы
                    </Typography>
                    { pressedEditButton ? <Field text={group_id} /> : <Label text={group_id} /> }
                </div>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Ссылка на ответственного за спортзал
                    </Typography>
                    { pressedEditButton ? <Field text={sport_resp_link} /> : <Label text={sport_resp_link} /> }
                </div>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Ссылка на ответственного за учебную комнату
                    </Typography>
                    { pressedEditButton ? <Field text={train_resp_link} /> : <Label text={train_resp_link} /> }
                </div>
                <div className={classes.row}>
                    <Typography className={classes.key}>
                        Ссылка на хранилище чеков
                    </Typography>
                    { pressedEditButton ? <Field text={receipts_link} /> : <Label text={receipts_link} /> }
                </div>

                <CardActions className={classes.actions}>
                    <Button className={classes.button} onClick={() => setPressedEditButton(!pressedEditButton)}>
                        { pressedEditButton ? "Сохранить" : "Редактировать" }
                    </Button>
                </CardActions>
            </Card>
        </div>
    )
}
