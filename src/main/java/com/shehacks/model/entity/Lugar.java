package com.shehacks.model.entity;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.io.Serializable;

@Data @NoArgsConstructor @AllArgsConstructor
@Entity
@Table(name = "tb_lugar")
public class Lugar implements Serializable {

	private static final long serialVersionUID = 1L;

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@JsonProperty("nome")
	private String nome;
	@JsonProperty("endereco")
	private String endereco;
	@JsonProperty("horarioAbre")
	private String horarioAbre;
	@JsonProperty("horarioFecha")
	private String horarioFecha;
}
