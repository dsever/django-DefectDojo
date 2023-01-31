## Parameters

### Global settings

| Name                             | Description                                                                                                | Value                               |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `createSecret`                   | create defectdojo specific secret                                                                          | `false`                             |
| `createRabbitMqSecret`           | create rabbitmq secret in defectdojo chart, outside of rabbitmq chart                                      | `false`                             |
| `createRedisSecret`              | create redis secret in defectdojo chart, outside of redis chart                                            | `false`                             |
| `createMysqlSecret`              | create mysql secret in defectdojo chart, outside of mysql chart                                            | `false`                             |
| `createPostgresqlSecret`         | create postgresql secret in defectdojo chart, outside of postgresql chart                                  | `false`                             |
| `createPostgresqlHaSecret`       | create postgresql-ha secret in defectdojo chart, outside of postgresql-ha chart                            | `false`                             |
| `createPostgresqlHaPgpoolSecret` | create postgresql-ha-pgpool secret in defectdojo chart, outside of postgresql-ha chart                     | `false`                             |
| `trackConfig`                    | will automatically respin application pods in case of config changes detection, disabled (default)/enabled | `disabled`                          |
| `database`                       | Option to use "postgresql" or "mysql" database type, by default "mysql" is chosen                          | `postgresql`                        |
| `host`                           | Primary hostname of instance                                                                               | `defectdojo.default.minikube.local` |


### Image

| Name               | Description                                                                                            | Value        |
| ------------------ | ------------------------------------------------------------------------------------------------------ | ------------ |
| `imagePullPolicy`  | Kubernetes image pull policy, https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy | `Always`     |
| `repositoryPrefix` | Where to pull the defectDojo images from. Defaults to "defectdojo/*" repositories on hub.docker.com    | `defectdojo` |
| `imagePullSecrets` | Image pull secret                                                                                      | `[]`         |
| `tag`              | Image tag                                                                                              | `latest`     |
| `podLabels`        | Additional labels to add to the pods                                                                   | `{}`         |
| `securityContext`  | Pod Security Context                                                                                   | `undefined`  |


### Database




### Message Broker

| Name           | Description                                                                                      | Value |
| -------------- | ------------------------------------------------------------------------------------------------ | ----- |
| `extraConfigs` | Add extra variables not predefined by helm config it is possible to define in extraConfigs block | `{}`  |


## Upgrading
