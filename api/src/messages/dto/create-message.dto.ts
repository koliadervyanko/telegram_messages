export class CreateMessageDto {
  username: string | null;
  message: string;
  name: string | null;
  link: string;
  date: string;
  replies: CreateMessageDto[] | null;
  messageId: number;
  keyWord: string;
}
