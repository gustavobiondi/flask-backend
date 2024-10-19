import React, { useContext } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import { UserContext } from '../UserContext'; // Import the context

export default class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      senha: '',
    };
  }

  static contextType = UserContext; // Assign contextType to access context

  mandarValores(username, senha) {
    fetch('http://192.168.1.36:5000/verificar_username', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username,
        senha: senha,
      }),
    })
      .then((response) => response.json()) // Convert response to JSON
      .then((data) => {
        if (data.data) {
          // Se o backend retornar True, update the user context
          const { setUser } = this.context; // Access setUser from context
          setUser({ username: this.state.username, cargo: data.cargo }); // Update the global user state
        } else {
          alert('Usuário ou senha inválidos');
        }
      })
      .catch((error) => {
        console.error('Erro:', error);
      });
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Login</Text>
        <TextInput
          placeholder="Usuario"
          value={this.state.username}
          onChangeText={(username) => this.setState({ username })}
        />
        <TextInput
          secureTextEntry={true}
          placeholder="Senha"
          value={this.state.senha}
          onChangeText={(senha) => this.setState({ senha })}
        />
        <Button
          title="Entrar"
          onPress={() => this.mandarValores(this.state.username, this.state.senha)}
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
});
