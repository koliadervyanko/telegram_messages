import { StringOrNull } from '../types/types';

export class CreateMessageDto {
  groupLink: string;
  keyWord: string;
  comment: string;
  username: StringOrNull;
  name: StringOrNull;
  date: string;
  hasReplies: boolean;
}
